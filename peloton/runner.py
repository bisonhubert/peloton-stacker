import sys

from seed.sets import current_workout_set
from services.user_input import UserInput
from stack.stack_builder import StackBuilder

class Runner:
    def __init__(self):
        self.day = None
        self.week = None
        self.current_workout_set = current_workout_set

    def _set_week_and_day(self):
        week = next(filter(lambda x: "--w=" in x, sys.argv), None)
        if week is not None:
            self.week = int(week.split("=")[-1])
            day = next(filter(lambda x: "--d=" in x, sys.argv), None)
            if day is None:
                self.day = 1
            else:
                self.day = int(day.split("=")[-1])
        else:
            ui = UserInput()
            ui.run()
            self.day = ui.day
            self.week = ui.week

    def _add_classes(self):
        # this should eventually load workout_set as JSON or a Python dict
        # for now just adds a single class
        StackBuilder(workout_set=self.current_workout_set, day=self.day, week=self.week).run()

    def _empty_stack(self):
        StackBuilder(self.current_workout_set)._empty()

    def run(self):
        if "--empty" in sys.argv:
            self._empty_stack()
        else:
            self._set_week_and_day()
            self._add_classes()


runner = Runner()
runner.run()


# Questions
# 1. How to organize a class series (BYPZ, CYC, strength, custom) with IDs, instructor names, etc?


# Sample use case
# 1. Run runner.py
# 2. Asks week and day
# 3. Adds items for that to the stack (so the weeks and days have to be pre-computed)


# Features
# 1. Bypass user prompt by supplying week and day in command
# 2. Test runner
# 3. Auto-generate (cookie-cutter) new workout set file with filename and auto-gen date

# Day
# classes to add for a day of the week (M-Sun)

# Week
# series of days, can select a week number (1-4) and day number (1-7)

# Stack
# used to add classes to a stack or view the current
