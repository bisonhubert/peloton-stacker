import json
import os

from workout.day import Day
from workout.week import Week
from workout.workout_set import WorkoutSet

script_dir = os.path.dirname(__file__)
current_workout_set_filename = '2021_07_23_bypz_cyc_total_strength'
rel_path = f"sets/{current_workout_set_filename}.json"
abs_file_path = os.path.join(script_dir, rel_path)

current_workout_set = None

with open(abs_file_path, 'r') as f:
    current_workout_set = json.load(f)
