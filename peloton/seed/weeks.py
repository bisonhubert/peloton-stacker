from seed.days import Days
from workout.week import Week

def _get_ride_tokens(rides):
    return [r.token for r in rides]

class Weeks:
    BYPZ_STRENGTH_CYC_WEEK_1 = [Week(1, days=Days.AW_STRENGTH_DAYS)]
