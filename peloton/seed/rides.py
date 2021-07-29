from ride.ride_data import Cycling, Strength, Stretches
from ride.ride import Ride

def _make_ride(ride_data):
    return Ride(slug=ride_data.get('slug'), token=ride_data.get('token'))

def _get_rides(rides=None):
    if rides is None:
        return None
    return [_make_ride(ride_data) for ride_data in rides]

class StretchRides:
    FULL_BODY = [_make_ride(ride_data) for ride_data in Stretches.FULL_BODY_10_MIN]
    FOAM_ROLLING = [_make_ride(ride_data) for ride_data in Stretches.FOAM_ROLLING]
    POST_RIDE_5_MIN = [_make_ride(ride_data) for ride_data in Stretches.POST_RIDE_5_MIN]

class StrengthRides:
    AW_DAY_1 = _get_rides(Strength.AW_DAY_1)
    AW_DAY_2 = None
    AW_DAY_3 = None
    AW_DAY_4 = None
    # unmade
    # AW_DAY_2 = _get_rides(Strength.AW_DAY_2)
    # AW_DAY_3 = _get_rides(Strength.AW_DAY_3)
    # AW_DAY_4 = _get_rides(Strength.AW_DAY_4)

# BYPZ
# current_workout_set = [
#     Cycling.week_4_day_1,
#     Cycling.week_4_day_2,
#     Cycling.week_4_day_3,
#     Cycling.week_5_day_1,
#     Cycling.week_5_day_2,
#     Cycling.week_5_day_3_part_1,
#     Cycling.week_5_day_3_part_2,
# ]

# 5min Cool Down Rides
# current_workout_set = [
#     Cycling.ally_5_min_1,
#     Cycling.ally_5_min_2,
#     Cycling.ben_5_min,
#     Cycling.emma_5_min,
#     Cycling.robin_5_min,
#     Cycling.cody_5_min,
#     Cycling.dennis_5_min,
#     Cycling.tunde_5_min_1,
#     Cycling.tunde_5_min_2,
# ]

# 10min Cool Down Rides
# current_workout_set = [
#     Cycling.alex_10_min,
#     Cycling.dennis_10_min,
#     Cycling.ally_10_min,
#     Cycling.robin_10_min,
#     Cycling.olivia_10_min,
#     Cycling.hannah_10_min,
#     Cycling.tunde_10_min_1,
#     Cycling.tunde_10_min_2,
# ]
