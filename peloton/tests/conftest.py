import pytest

from peloton.workout.day import Day
from peloton.workout.ride import Ride


@pytest.fixture
def ride_1():
    return Ride("test-token-1")


@pytest.fixture
def ride_2():
    return Ride("test-token-2")


@pytest.fixture
def days(ride_1, ride_2):
    return [Day(i + 1, rides=[ride_1, ride_2]) for i in range(7)]
