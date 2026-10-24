import datetime as dt
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


@dataclass
class Slot:
    day: str
    program: str
    title: str
    class_id: str = None
    search_url: str = None


@dataclass
class Program:
    name: str
    workouts: list
    supplements: list = field(default_factory=list)


@dataclass
class Cycle:
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
    for workout in data["workouts"]:
        if workout["day"] not in DAYS:
            raise ValueError(f"{path}: {workout['day']} is not a day of the week")
    return Program(data["name"], data["workouts"], data.get("supplements", []))


def load_cycle(path, programs_dir):
    data = tomllib.loads(Path(path).read_text())
    if data["start"].weekday() != 0:
        raise ValueError(f"{path}: start {data['start']} is not a Monday")
    if not 1 <= data["weeks"] <= 6:
        raise ValueError(f"{path}: weeks must be 1-6")
    programs = [load_program(Path(programs_dir) / f"{p}.toml") for p in data["programs"]]
    return Cycle(Path(path).stem, data["start"], data["weeks"], programs)


def week_monday(today):
    return today - dt.timedelta(days=today.weekday())


def active_cycle(cycles, monday):
    for cycle in cycles:
        if cycle.start <= monday < cycle.end:
            return cycle
    raise LookupError(f"No cycle covers the week of {monday}")


def week_slots(cycle):
    slots = []
    for day in DAYS:
        for program in cycle.programs:
            for workout in program.workouts:
                if workout["day"] != day:
                    continue
                slots.append(Slot(day, program.name, workout["title"], class_id=workout["class"]))
                for supplement in program.supplements:
                    slots.append(
                        Slot(day, program.name, supplement["title"], search_url=supplement["search"])
                    )
    return slots
