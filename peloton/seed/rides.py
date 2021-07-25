from ride.ride_data import Cycling, Stretches
from ride.ride import Ride

def _make_ride(ride_data):
    return Ride(slug=ride_data.get('slug'), token=ride_data.get('token'))

class StretchRides:
    FULL_BODY = [_make_ride(ride_data) for ride_data in Stretches.FULL_BODY_10_MIN]
    FOAM_ROLLING = [_make_ride(ride_data) for ride_data in Stretches.FOAM_ROLLING]
    POST_RIDE_5_MIN = [_make_ride(ride_data) for ride_data in Stretches.POST_RIDE_5_MIN]

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
