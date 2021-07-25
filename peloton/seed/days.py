from seed.rides import StretchRides
from workout.day import Day

foam_rolling_ride_ids = [r for r in StretchRides.FOAM_ROLLING]
foam_rolling_ride_ids.append(StretchRides.FULL_BODY[-1])

class Days:
    REST_DAY = Day(7, rides=foam_rolling_ride_ids)
