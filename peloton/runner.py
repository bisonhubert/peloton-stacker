from classes.instructors import adrian_williams
from stack import Stack
from user_input import UserInput



# prompt
# ui = UserInput()
# ui.run()

# test adding class
full_body_stretch_classes = adrian_williams.FullBodyStretchClass().get_class_ids()
stack = Stack([full_body_stretch_classes[-1]])
stack.run()


# Questions
# 1. How to organize a class series (BYPZ, CYC, strength, custom) with IDs, instructor names, etc?


# Sample use case
# 1. Run runner.py
# 2. Asks week and day
# 3. Adds items for that to the stack (so the weeks and days have to be pre-computed)


# Features
# 1. Bypass user prompt by supplying week and day in command

# Day
# classes to add for a day of the week (M-Sun)

# Week
# series of days, can select a week number (1-4) and day number (1-7)

# Stack
# used to add classes to a stack or view the current
