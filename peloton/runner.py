from graphql_ids import AdrianWilliams
from ride import Ride
from stack.stack_builder import StackBuilder
from user_input import UserInput
# from workout.current_workout_set import current_workout_set

current_workout_set = [Ride(AdrianWilliams.full_body_stretch_1, AdrianWilliams.slug).graphql_id]

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


    def run(self):
        # self._run_user_input()
        self._add_classes()


runner = Runner()
runner.run()


# test adding class
# full_body_stretch_classes = adrian_williams.FullBodyStretchClass().get_class_ids()
# stack = StackBuilder([full_body_stretch_classes[-1]])
# stack.run()


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
