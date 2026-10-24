import datetime as dt
import random
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

STACK_LIMIT = 10
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


@dataclass
class Slot:
    day: str
    program: str
    title: str = None
    class_ref: str = None
    search_url: str = None
    shuffle: tuple = None


@dataclass
class Program:
    name: str
    workouts: list = field(default_factory=list)
    supplements: list = field(default_factory=list)
    days: list = field(default_factory=list)
    rotation: list = field(default_factory=list)
    shuffles: list = field(default_factory=list)

    def workouts_for(self, week, block_start):
        if self.shuffles:
            return [self._shuffle(shuffle, week, block_start) for shuffle in self.shuffles]
        if not self.rotation:
            return self.workouts
        offset = (week - 1) * len(self.days)
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

    @property
    def end(self):
        return self.start + dt.timedelta(weeks=self.weeks)

    def week_of(self, monday):
        return (monday - self.start).days // 7 + 1


def load_program(path):
    data = tomllib.loads(Path(path).read_text())
    program = Program(
        data["name"],
        data.get("workouts", []),
        data.get("supplements", []),
        data.get("days", []),
        data.get("rotation", []),
        data.get("shuffles", []),
    )
    if sum(map(bool, (program.workouts, program.rotation, program.shuffles))) != 1:
        raise ValueError(f"{path}: set one of workouts, rotation, or shuffles")
    if program.rotation and not program.days:
        raise ValueError(f"{path}: rotation needs days")
    for shuffle in program.shuffles:
        if ("classes" in shuffle) == ("search" in shuffle):
            raise ValueError(f"{path}: shuffle on {shuffle['day']} needs either classes or search")
    for day in program.days + [w["day"] for w in program.workouts + program.shuffles]:
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
    return Block(Path(path).stem, data["start"], data["weeks"], programs)


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


def active_block(blocks, monday):
    for block in blocks:
        if block.start <= monday < block.end:
            return block
    raise LookupError(f"No block covers the week of {monday}")


def week_slots(block, week):
    slots = []
    for day in DAYS:
        for program in block.programs:
            for workout in program.workouts_for(week, block.start):
                if workout["day"] != day:
                    continue
                slots.append(
                    Slot(
                        day,
                        program.name,
                        workout.get("title"),
                        class_ref=workout.get("class"),
                        search_url=workout.get("search"),
                        shuffle=workout.get("shuffle"),
                    )
                )
                for supplement in program.supplements:
                    slots.append(
                        Slot(day, program.name, supplement["title"], search_url=supplement["search"])
                    )
    return slots


def window(blocks, today, limit):
    classes = []
    date = today
    while True:
        try:
            block = active_block(blocks, week_monday(date))
        except LookupError:
            if date > today:
                return classes
            raise
        day = DAYS[date.weekday()]
        slots = [s for s in week_slots(block, block.week_of(week_monday(date))) if s.day == day]
        if len(classes) + len(slots) > limit:
            if date > today:
                return classes
            raise ValueError(f"{date} has {len(slots)} classes, more than the {limit} a stack holds")
        classes += [(date, block, slot) for slot in slots]
        date += dt.timedelta(days=1)
