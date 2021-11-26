class GetRide:

    def get_ride(self, day=None):
        if day is None:
            return
        if day == 0:
            return self.DAY_1
        if day == 1:
            return self.DAY_2
        if day == 2:
            return self.DAY_3
        if day == 3:
            return self.DAY_4
        if day == 4:
            return self.DAY_5
        if day == 5:
            return self.DAY_6
        if day == 6:
            return self.DAY_7

