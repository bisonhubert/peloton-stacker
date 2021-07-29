from seed.rides import StrengthRides, StretchRides
from workout.day import Day

foam_rolling_ride_ids = [r for r in StretchRides.FOAM_ROLLING]
foam_rolling_ride_ids.append(StretchRides.FULL_BODY[-1])


def _get_ride_ids(rides):
    return [r for r in rides]


class Days:
    REST_DAY = Day(7, rides=foam_rolling_ride_ids)
    AW_STRENGTH_DAYS = [
        None,
        Day(2, rides=StrengthRides.AW_DAY_1),
        Day(3, rides=StrengthRides.AW_DAY_2),
        Day(4, rides=StrengthRides.AW_DAY_3),
        Day(5, rides=StrengthRides.AW_DAY_4),
        None,
        REST_DAY,
    ]
