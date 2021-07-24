# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_week ride=test-token as dict'] = {
    'token': 'test-token'
}

snapshots['test_week ride=test-token as string'] = 'ride=test-token'
