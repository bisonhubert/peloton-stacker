# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_day Friday as dict'] = {
    'name': 'Friday',
    'number': 5,
    'rides': [
        GenericRepr('<peloton.workout.ride.Ride object at 0x100000000>'),
        GenericRepr('<peloton.workout.ride.Ride object at 0x100000000>')
    ]
}

snapshots['test_day Friday as string'] = 'name=Friday'

snapshots['test_day Monday as dict'] = {
    'name': 'Monday',
    'number': 1,
    'rides': [
        GenericRepr('<peloton.workout.ride.Ride object at 0x100000000>'),
        GenericRepr('<peloton.workout.ride.Ride object at 0x100000000>')
    ]
}

snapshots['test_day Monday as string'] = 'name=Monday'

snapshots['test_day Saturday as dict'] = {
    'name': 'Saturday',
    'number': 6,
    'rides': [
        GenericRepr('<peloton.workout.ride.Ride object at 0x100000000>'),
        GenericRepr('<peloton.workout.ride.Ride object at 0x100000000>')
    ]
}

snapshots['test_day Saturday as string'] = 'name=Saturday'

snapshots['test_day Thursday as dict'] = {
    'name': 'Thursday',
    'number': 4,
    'rides': [
        GenericRepr('<peloton.workout.ride.Ride object at 0x100000000>'),
        GenericRepr('<peloton.workout.ride.Ride object at 0x100000000>')
    ]
}

snapshots['test_day Thursday as string'] = 'name=Thursday'

snapshots['test_day Tuesday as dict'] = {
    'name': 'Tuesday',
    'number': 2,
    'rides': [
        GenericRepr('<peloton.workout.ride.Ride object at 0x100000000>'),
        GenericRepr('<peloton.workout.ride.Ride object at 0x100000000>')
    ]
}

snapshots['test_day Tuesday as string'] = 'name=Tuesday'

snapshots['test_day Wednesday as dict'] = {
    'name': 'Wednesday',
    'number': 3,
    'rides': [
        GenericRepr('<peloton.workout.ride.Ride object at 0x100000000>'),
        GenericRepr('<peloton.workout.ride.Ride object at 0x100000000>')
    ]
}

snapshots['test_day Wednesday as string'] = 'name=Wednesday'
