import pytest

from peloton.workout.day import Day

@pytest.fixture
def monday():
    return Day(1)
