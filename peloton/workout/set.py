class Set:
    def __init__(self, weeks=None):
        self.week = None
        self.day = None
        self.weeks = [week for week in weeks] if weeks is not None else None

    def _set_week(self, number):
        if self.weeks is not None:
            for week in self.weeks:
                if hasattr(week, 'number') and week.number == number:
                    self.week = week

    def _set_day(self, number):
        if self.week is not None:
            for day in self.week.days:
                if hasattr(day, 'number') and day.number == number:
                    self.day = day
        
    def get_ride_tokens(self, week=1, day=1):
        self._set_week(week)
        self._set_day(day)
        if self.day is None:
            return None
        return [ride.token for ride in self.day.rides]
