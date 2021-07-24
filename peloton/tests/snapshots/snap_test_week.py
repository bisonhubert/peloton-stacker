# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_week week=1 as dict'] = {
    'days': [
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>')
    ],
    'number': 1
}

snapshots['test_week week=1 as string'] = 'week=1'

snapshots['test_week week=2 as dict'] = {
    'days': [
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>')
    ],
    'number': 2
}

snapshots['test_week week=2 as string'] = 'week=2'

snapshots['test_week week=3 as dict'] = {
    'days': [
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>')
    ],
    'number': 3
}

snapshots['test_week week=3 as string'] = 'week=3'

snapshots['test_week week=4 as dict'] = {
    'days': [
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>')
    ],
    'number': 4
}

snapshots['test_week week=4 as string'] = 'week=4'

snapshots['test_week week=5 as dict'] = {
    'days': [
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>'),
        GenericRepr('<peloton.workout.day.Day object at 0x100000000>')
    ],
    'number': 5
}

snapshots['test_week week=5 as string'] = 'week=5'
