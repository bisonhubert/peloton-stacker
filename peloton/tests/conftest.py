import pytest

from peloton.workout.day import Day

@pytest.fixture
def days():
    return [Day(i + 1) for i in range(7)]
