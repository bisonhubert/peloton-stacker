import sys

from seeds import rides
from stack.stack_builder import StackBuilder

class Runner:
    def __init__(self):
        self.day = None

    def _set_week_and_day(self):
        import pdb;pdb.set_trace()
        self.day = ''

    def _add_classes(self, payload=None):
        StackBuilder().run(payload=payload)

    def _empty_stack(self):
        StackBuilder()._empty()

    def run(self):
        if "--empty" in sys.argv:
            self._empty_stack()
        else:
            self._set_week_and_day()
            self._add_classes(payload=rides.CrushYourCore.DAY_1)


runner = Runner()
runner.run()
