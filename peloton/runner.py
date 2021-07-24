from ride_ids import Stretches
from stack.stack_builder import StackBuilder
from services.user_input import UserInput

current_workout_set = [
    Stretches.full_body_stretch_1,
    Stretches.foam_rolling_chest_and_back,
    Stretches.foam_rolling_glutes,
    Stretches.foam_rolling_quads,
    Stretches.foam_rolling_hamstrings,
    Stretches.foam_rolling_calves,
    Stretches.full_body_stretch_6,
]


class Runner:
    def __init__(self):
        self.day = None
        self.week = None
        self.current_workout_set = current_workout_set

    def _run_user_input(self):
        ui = UserInput()
        ui.run()
        self.day = ui.day
        self.week = ui.week

    def _add_classes(self):
        # this should eventually load workout_set as JSON or a Python dict
        # for now just adds a single class
        StackBuilder(self.current_workout_set).run()

    def _empty_stack(self):
        StackBuilder(self.current_workout_set)._empty()

    def run(self):
        # self._run_user_input()
        self._add_classes()
        # self._empty_stack()


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
