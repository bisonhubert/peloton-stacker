import pytest

from peloton.workout.day import Day


def test_day(snapshot, ride_1, ride_2):
    for i in range(6):
        day = Day(i + 1, [ride_1, ride_2])
        snapshot.assert_match(day.__dict__, f"{day.name} as dict")
        snapshot.assert_match(str(day), f"{day.name} as string")

def test_day_with_invalid_number():
    with pytest.raises(Exception) as e:
        Day()
        Day(0)
        Day(8)
        Day('1')
