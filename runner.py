import datetime as dt
import sys

from stack.stack_builder import StackBuilder

class Runner:
    PST = dt.timezone(dt.timedelta(hours=-8))

    def __init__(self):
        self.day = None

    def _set_day(self):
        now = dt.datetime(1,1,1).now(self.PST)
        self.day = now.weekday()

    def _add_classes(self):
        StackBuilder(day=self.day).run()

    def _empty_stack(self):
        StackBuilder()._empty()

    def run(self):
        if "--empty" in sys.argv:
            self._empty_stack()
        else:
            self._set_day()
            self._add_classes()


runner = Runner()
runner.run()