import datetime as dt
import random
import tomllib
from dataclasses import dataclass, field, replace
from pathlib import Path

STACK_LIMIT = 25
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


@dataclass
class Slot:
    day: str
    program: str
    title: str = None
    class_ref: str = None
    search_url: str = None
    arms_search_url: str = None
    shuffle: tuple = None


@dataclass
class Program:
    name: str
    workouts: list = field(default_factory=list)
    supplements: list = field(default_factory=list)
    days: list = field(default_factory=list)
    rotation: list = field(default_factory=list)
    shuffles: list = field(default_factory=list)
    off_days: list = field(default_factory=list)
    strength: bool = False

    def workouts_for(self, week, block_start, done=None):
        if self.shuffles:
            return [self._shuffle(shuffle, week, block_start) for shuffle in self.shuffles]
        if not self.rotation:
            return self.workouts
        offset = (week - 1) * len(self.days) if done is None else done.get(self.name, 0)
        return [
            {"day": day, "class": self.rotation[(offset + i) % len(self.rotation)]}
            for i, day in enumerate(self.days)
        ]

    def _shuffle(self, shuffle, week, block_start):
        seed = f"{block_start}:{self.name}:{shuffle['day']}"
        workout = {"day": shuffle["day"], "title": shuffle.get("title")}
        if "classes" in shuffle:
            return {**workout, "class": pick(shuffle["classes"], seed, week)}
        return {**workout, "search": shuffle["search"], "shuffle": (seed, week, block_start)}


@dataclass
class Block:
    name: str
    start: dt.date
    weeks: int
    programs: list
    breaks: list = field(default_factory=list)
    done: dict = None

    @property
    def end(self):
        return self.start + dt.timedelta(weeks=self.weeks + len(self.breaks))

    @property
    def strength(self):
        return any(program.strength for program in self.programs)

    def week_of(self, monday):
        return (monday - self.start).days // 7 + 1 - sum(b < monday for b in self.breaks)

    def monday_of(self, week):
        monday = self.start + dt.timedelta(weeks=week - 1)
        for b in sorted(self.breaks):
            if b <= monday:
                monday += dt.timedelta(weeks=1)
        return monday

    def heading(self, week):
        if self.weeks:
            return f"{self.name}, week {week} of {self.weeks}"
        return f"{self.name}, week {week}"


def load_program(path):
    data = tomllib.loads(Path(path).read_text())
    program = Program(
        data["name"],
        data.get("workouts", []),
        data.get("supplements", []),
        data.get("days", []),
        data.get("rotation", []),
        data.get("shuffles", []),
        data.get("off_days", []),
        data.get("strength", False),
    )
    if sum(map(bool, (program.workouts, program.rotation, program.shuffles))) != 1:
        raise ValueError(f"{path}: set one of workouts, rotation, or shuffles")
    if program.rotation and not program.days:
        raise ValueError(f"{path}: rotation needs days")
    for shuffle in program.shuffles:
        if ("classes" in shuffle) == ("search" in shuffle):
            raise ValueError(f"{path}: shuffle on {shuffle['day']} needs either classes or search")
    for day in program.days + program.off_days + [w["day"] for w in program.workouts + program.shuffles]:
        if day not in DAYS:
            raise ValueError(f"{path}: {day} is not a day of the week")
    return program


def load_block(path, programs_dir):
    data = tomllib.loads(Path(path).read_text())
    if data["start"].weekday() != 0:
        raise ValueError(f"{path}: start {data['start']} is not a Monday")
    if not 1 <= data["weeks"] <= 6:
        raise ValueError(f"{path}: weeks must be 1-6")
    programs = [load_program(Path(programs_dir) / f"{p}.toml") for p in data["programs"]]
    block = Block(Path(path).stem, data["start"], data["weeks"], programs, data.get("breaks", []))
    for b in block.breaks:
        if b.weekday() != 0:
            raise ValueError(f"{path}: break {b} is not a Monday")
        if not block.start < b < block.end - dt.timedelta(weeks=1):
            raise ValueError(f"{path}: break {b} is not between two weeks of the block")
    if len(set(block.breaks)) != len(block.breaks):
        raise ValueError(f"{path}: breaks repeat")
    return block


def load_off(path, programs_dir):
    data = tomllib.loads(Path(path).read_text())
    programs = [load_program(Path(programs_dir) / f"{p}.toml") for p in data["programs"]]
    programs = [replace(p, days=p.off_days or p.days) for p in programs]
    return Block(Path(path).stem, None, None, programs)


def pick(items, seed, week):
    turn, index = divmod(week - 1, len(items))
    return _turn(items, seed, turn)[index]


def _turn(items, seed, turn):
    order = sorted(items)
    random.Random(f"{seed}:{turn}").shuffle(order)
    if turn and order[0] == _turn(items, seed, turn - 1)[-1]:
        order.append(order.pop(0))
    return order


def week_monday(today):
    return today - dt.timedelta(days=today.weekday())


def active_block(blocks, off, monday):
    for block in blocks:
        if block.start <= monday < block.end:
            done = rotation_done(block, off, monday)
            if monday in block.breaks:
                start = monday
                while start - dt.timedelta(weeks=1) in block.breaks:
                    start -= dt.timedelta(weeks=1)
                return replace(off, name=f"{block.name} break", start=start, done=done)
            return replace(block, done=done)
    ended = [block.end for block in blocks if block.end <= monday]
    if not ended:
        raise LookupError(f"No block covers the week of {monday}")
    return replace(off, start=max(ended))


def rotation_done(block, off, monday):
    done = {}
    week = block.start
    while week < monday:
        programs = off.programs if week in block.breaks else block.programs
        for program in programs:
            if program.rotation:
                done[program.name] = done.get(program.name, 0) + len(program.days)
        week += dt.timedelta(weeks=1)
    return done


def week_slots(block, week):
    slots = []
    for day in DAYS:
        for program in block.programs:
            for workout in program.workouts_for(week, block.start, block.done):
                if workout["day"] != day:
                    continue
                slots.append(
                    Slot(
                        day,
                        program.name,
                        workout.get("title"),
                        class_ref=workout.get("class"),
                        search_url=workout.get("search"),
                        arms_search_url=None if block.strength else workout.get("arms_search"),
                        shuffle=workout.get("shuffle"),
                    )
                )
                for supplement in program.supplements:
                    slots.append(
                        Slot(day, program.name, supplement["title"], search_url=supplement["search"])
                    )
    return slots


def rest_of_week(blocks, off, today):
    monday = week_monday(today)
    block = active_block(blocks, off, monday)
    slots = week_slots(block, block.week_of(monday))
    classes = [
        (monday + dt.timedelta(days=DAYS.index(slot.day)), block, slot)
        for slot in slots
        if DAYS.index(slot.day) >= today.weekday()
    ]
    if len(classes) > STACK_LIMIT:
        raise ValueError(f"{today} to Sunday has {len(classes)} classes, more than a stack holds")
    return classes
