import requests

from peloton.account import Account
from peloton.stack.constants import Api, Operation, Queries


class StackBuilder:
    # def __init__(self, workout_set=None, day=None, week=None):
    def __init__(self):
        self.session = None
        self.ride_tokens = None
        # self.workout_set = workout_set
        # self.day = day
        # self.week = week
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

    def _add_ride(self, payload=None):
        # payload = self._get_payload(Operation.ADD, ride_token)
        self.session.post(Api.ENDPOINT, json=payload)

    def _empty(self):
        payload = self._get_payload(Operation.EMPTY)
        resp = self.session.post(Api.ENDPOINT, json=payload)

    def _set_ride_tokens(self):
        if self.workout_set is not None:
            self.ride_tokens = self.workout_set.get_ride_tokens(week=self.week, day=self.day)

    def _get(self):
        pass

    def _remove_ride(self):
        pass

    def run(self, payload=None):
        if payload is not None:
            self._add_ride(payload=payload)
        # self._set_ride_tokens()
        # if self.ride_tokens is not None:
        #     for ride_token in self.ride_tokens:
        #         self._add_ride(ride_token)
