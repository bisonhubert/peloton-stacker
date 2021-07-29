from seed.weeks import Weeks
from workout.set import Set

def _make_set(weeks):
    return Set(weeks=weeks)

class Sets:
    BYPZ_STRENGTH_CYC = _make_set(Weeks.BYPZ_STRENGTH_CYC_WEEK_1)

current_workout_set = Sets.BYPZ_STRENGTH_CYC
