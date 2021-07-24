import pytest

from peloton.workout.week import Week


def test_week(snapshot, days):
    for i in range(5):
        week = Week(i + 1, days=days)
        snapshot.assert_match(week.__dict__, f"{week} as dict")
        snapshot.assert_match(str(week), f"{week} as string")

def test_week_with_invalid_number():
    with pytest.raises(Exception) as e:
        Week()
        Week(0)
        Week(6)
        Week('1')
