from peloton.workout.ride import Ride


def test_week(snapshot):
    ride = Ride('test-token')
    snapshot.assert_match(ride.__dict__, f"{ride} as dict")
    snapshot.assert_match(str(ride), f"{ride} as string")
