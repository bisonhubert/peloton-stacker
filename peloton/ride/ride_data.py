def _get_token(ride_token):
    ride = list(filter(lambda x: x.get('slug') == ride_token, Stretches.FULL_BODY_10_MIN))
    if len(ride) == 0:
        return
    return ride[0].get('token')

class Stretches:
    FULL_BODY_10_MIN = [
        {
            "token": "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICJkZGM1MTlhZjMxMWU0ZTg3YmExNjY5Zjk3OTdhMjk0OSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9",
            "slug": "aw-fbs-1",
        },
        {
            "token": "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICIxZTNjZWY3NGZkOTM0ZjdjYmM4NGY0MWFhZWZkNDQ2MiIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9",
            "slug": "aw-fbs-2",
        },
        {
            "token": "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICIyYmYzOTIwMTUwZDQ0NDg1YjAyMmY3NTQ4YzIwZGI4NyIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9",
            "slug": "aw-fbs-3",
        },
        {
            "token": "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICIxZjM3M2QxMWI4MWM0YWZlOGI2MjdmY2E2OTRhMjhlNSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9",
            "slug": "aw-fbs-4",
        },
        {
            "token": "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICI4ZjgwZDZjZmFkMmI0YjEzOGE0NjljY2UxMDZmZWExOSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9",
            "slug": "aw-fbs-5",
        },
        {
            "token": "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICI5N2RmMzdmYzkxMGE0ZWNmYjZkYjEwYzJiOTliNWI5OSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9",
            "slug": "aw-fbs-6",
        },
        {
            "token": "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICIxZGY4YTViZjEzZDY0YWMyOGEyMTk4ZjU5Y2JjY2Y1YSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9",
            "slug": "aw-fbs-7",
        },
    ]
    FOAM_ROLLING = [
        {
            "slug": "hc-fr-chest-back",
            "token": "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICIyNzlkMDdmYTc2Mzk0NzhkYjgwZjRkYTZmYTQ4NDRmYSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9",
        },
        {
            "slug": "hc-fr-glutes",
            "token": "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICI1MWNkNTFhMTY2ODE0NmU5YmFkZWUyMzUzOGFmNTVjMCIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9",
        },
        {
            "slug": "hc-fr-quads",
            "token": "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICI2NmM3ZGRkNGZjMzg0ZmZiYTc1YzY0ZjZlNDQ5MjZjZCIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9",
        },
        {
            "slug": "hc-fr-hamstrings",
            "token": "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICI1NGY1MjBlYjZjODU0NTFjYjE0ZTk0NjNlZTcyYzRmNSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9",
        },
        {
            "slug": "hc-fr-calves",
            "token": "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICIwYTIzNTFhYTViNjA0ODIzOTdhMDA0ZGZhYjI2OWRiYSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9",
        },
    ]
    POST_RIDE_5_MIN = [
        {
            "slug": "tunde-prs-5min",
            "token": "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICI5OGRhZWY1NDNlNTI0M2ZmYmYxYmU4MzZiNTI1OWU0NiIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9",
        },
        {
            "slug": "wilpers-prs-5min",
            "token": "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICJmMDdiYmRjYjM2MDk0ZGFmYTYxYmQyNDY3Njk4ZDFkNCIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9",
        },
        {
            "slug": "emma-prs-5min",
            "token": "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICJjZWE5MTY2NTY1NGM0YWZjOGI5NDAyOGJjZjE0OTk2YyIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9",
        },
        {
            "slug": "ben-prs-5min",
            "token": "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICJiYjQ4MmU0MzM0MWU0OGM5YjhkMjlmN2ViZjU5OGQzMiIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9",
        },
        {
            "slug": "dennis-prs-5min",
            "token": "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICIzNTJhY2MyMjBlM2M0MDNlYjI5ZWM4ZDNjYTFkYjA3YSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9",
        },
        {
            "slug": "cody-prs-5min",
            "token": "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICJmYjQxYjZmMmU1YjQ0MjkwOWM0MGQ0ZjcxMjFlYzJiOSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9",
        },
        {
            "slug": "robin-prs-5min",
            "token": "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICJlYmQwNjkwNTUyNzg0ZmI3YWE3NzdlNTAxY2QwMTU0NiIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9",
        },
    ]


class Cycling:
    # todobison this should actually be a program
    # which would make this a set of week and day objects for n number of classes
    # Build Your Power Zones
    week_1_day_1 = ""
    week_1_day_2 = ""
    week_1_day_3 = ""
    week_2_day_1 = ""
    week_2_day_2 = ""
    week_2_day_3 = ""
    week_3_day_1 = ""
    week_3_day_2 = ""
    week_3_day_3 = ""
    week_4_day_1 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICI0YzIxMTBkZDRkZTc0YzliOWE0YTRlOTE3NjUwMTcwMiIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    week_4_day_2 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICI0N2FkMzc2NGZiZmI0Nzc0OTY3OTU4ODc0NDY1YmVlNCIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    week_4_day_3 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICIxYjc2OGVlMzc2YzU0NmFlOTI0OTNkODMwMWVlZWM4NSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    week_5_day_1 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICI3MjVkNjE4NTE2Njc0Zjc1ODFkNGQ1NjZmZTNmMDY1NSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    week_5_day_2 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICI0MzU1Y2JmODczNDY0OGMxYTI2YzJmNmQzNTQwMzVjNSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    week_5_day_3_part_1 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICIxZWFiZjcwYjIwNzQ0ZjQ4Yjk5MjU5ZjkzODg5Y2VkNSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    week_5_day_3_part_2 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICI0ZDMwMmJlZjQ5NTc0MTE4YTA3MTI2OWJlZDM4YmQzMCIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"

    # 5min Cool Down Rides
    ally_5_min_1 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICJiZTJhMTk3ZDk0ZTQ0YTZmODA2ZDdmNmUwM2YxNGIzZSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    ally_5_min_2 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICJkMzEwN2I1ZDBkNDE0YjkwYmYyMzFhOTg2Yzc2Nzk5MyIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    ben_5_min = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICJmZTdhMmNkZWU2Nzg0NGEzYTg4NWEzYTk1ZWEwOWE2NiIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    emma_5_min = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICI3YjlhNzY1MDIzMWM0NmExOTViZmEzOTBiY2FjZjMyYiIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    robin_5_min = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICJmMDUzYmM3NGY4MmQ0NTBlOWRmNjVlM2M5Yjg3YzNlZCIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    cody_5_min = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICJkM2JkNGEyNWE3ZmY0OTMyOTg3MTlhYjhjMDU5ZDNlNiIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    dennis_5_min = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICJmNTlkOTFmOWY1NDY0ZWRlYTVkMjM1NzFlM2NjMjM3NCIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    tunde_5_min_1 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICJhOTFjYTVmM2UyMGM0YWM2OTI1MDE3OTkwMzZlZTBjYiIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    tunde_5_min_2 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICI0MTI3MDI5OWJmYWM0Y2QzOGIzMGE1MTJiMDYzMTI3NyIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"

    # 10min Cool Down Rides
    alex_10_min = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICIyN2RlOTliOTYwNmQ0MTE0YjY5NjgyOTk3ZGFhNjJjOSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    dennis_10_min = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICJmNzhjY2NmNmMzN2U0OTBiYjliZjhlZWY2MDhhM2Y2NCIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    ally_10_min = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICJjODY1ZTc0MWY0ZGQ0ZDczODA0YTFlMWRlOGI0ZDI0NiIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    robin_10_min = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICI0NjY2YjgyZDI2N2Q0Njc5ODg4YTJjZDZkYWYzZTZmZSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    olivia_10_min = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICI5N2Q2MTY5MDE2Yjg0NDkxODliYzY4YWY3ZjAzMjIxYSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    hannah_10_min = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICI3ZmI4YzY2MWM2Mjk0YTFjYTFkNGM2NDc3MzAzNjNiOCIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    tunde_10_min_1 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICJiMjAyNDk0M2M5YTI0MTVkOGEwYWQwZTlkMTk4ZWM3NCIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    tunde_10_min_2 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICJjN2I5ZjUzYjQzMGY0OTdmODE2NjNmNTU1N2IyNTAwOSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"


class Strength:
    # Adrian Williams
    # https://www.pelobuddy.com/monthly-strength-stack-june-adrian-williams/
    AW_DAY_1 = [
        {
            "slug": "aw-d1-warmup",
            "token": "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICJkMTllMjdhMWQ3YWE0YTY3Yjc3MjRkMWM4MTc1OTZlYSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
        },
        {
            "slug": "aw-d1-lift",
            "token": "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICI3YjA4YzNjNjNmNTE0ZjhlOWU3MWNjOTQyMjJhYWQzMCIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
        },
        {
            "slug": "aw-d1-stretch",
            "token": _get_token('aw-fbs-3')
        }
    ]
    AW_DAY_2 = []
    AW_DAY_3 = []
    AW_DAY_4 = []
