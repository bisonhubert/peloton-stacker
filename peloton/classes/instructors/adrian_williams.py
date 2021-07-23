class FullBodyStretchClass:
    DAY_1 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICJkZGM1MTlhZjMxMWU0ZTg3YmExNjY5Zjk3OTdhMjk0OSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    DAY_2 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICIxZTNjZWY3NGZkOTM0ZjdjYmM4NGY0MWFhZWZkNDQ2MiIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    DAY_3 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICIyYmYzOTIwMTUwZDQ0NDg1YjAyMmY3NTQ4YzIwZGI4NyIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    DAY_4 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICIxZjM3M2QxMWI4MWM0YWZlOGI2MjdmY2E2OTRhMjhlNSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    DAY_5 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICI4ZjgwZDZjZmFkMmI0YjEzOGE0NjljY2UxMDZmZWExOSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    DAY_6 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICI5N2RmMzdmYzkxMGE0ZWNmYjZkYjEwYzJiOTliNWI5OSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    DAY_7 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICIxZGY4YTViZjEzZDY0YWMyOGEyMTk4ZjU5Y2JjY2Y1YSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"

    def get_class_id(self, day):
        if day == 1:
            return self.DAY_1
        elif day == 2:
            return self.DAY_2
        elif day == 3:
            return self.DAY_3
        elif day == 4:
            return self.DAY_4
        elif day == 5:
            return self.DAY_5
        elif day == 6:
            return self.DAY_6
        elif day == 7:
            return self.DAY_7

    def get_class_ids(self):
        return [
            self.DAY_1,
            self.DAY_2,
            self.DAY_3,
            self.DAY_4,
            self.DAY_5,
            self.DAY_6,
            self.DAY_7,
        ]
