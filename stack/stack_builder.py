import requests

from stack.account import Account
from stack.constants import Api, Operation, Queries
from seeds.crush_your_core import CrushYourCore
from seeds.rides import AT, AWS, CD, CYC, PRS

# cool down and post ride stretch
SEEDS = [CD, PRS]
# cool down, post ride stretch, core, and adrian williams stretch
# SEEDS = [CD, PRS, CYC, AWS]

class StackBuilder:
    def __init__(self, day=None):
        self.day = day
        self.session = None
        self.rides = None
        self._login()

    def _get_payload(self, operation, ride_token=None):
        payload = {}
        variables = {}
        if operation == Operation.ADD:
            payload["operationName"] = "AddClassToStack"
            payload["query"] = Queries.ADD
            variables = {"input": {"pelotonClassId": ride_token}}
        elif operation == Operation.EMPTY:
            payload["operationName"] = "ModifyStack"
            payload["query"] = Queries.CLEAR
            variables = {"input": {"pelotonClassIdList": []}}
        elif operation == Operation.VIEW:
            payload["operationName"] = "ViewUserStack"
            payload["query"] = Queries.GET
        payload["variables"] = variables
        return payload

    def _login(self):
        s = requests.Session()
        payload = {"username_or_email": Account.USERNAME, "password": Account.PASSWORD}
        s.post("https://api.onepeloton.com/auth/login", json=payload)
        self.session = s

    def _add_rides(self, payload=None):
        for payload in self.rides:
            self.session.post(Api.ENDPOINT, json=payload)

    def _empty(self):
        payload = self._get_payload(Operation.EMPTY)
        resp = self.session.post(Api.ENDPOINT, json=payload)

    def _set_rides(self):
        rides = []
        for seed in SEEDS:
            ride = seed.get_ride(day=self.day)
            if ride is not None:
                rides.append(ride)
        self.rides = rides

    def run(self):
        if self.day is not None:
            self._set_rides()
            self._add_rides()
