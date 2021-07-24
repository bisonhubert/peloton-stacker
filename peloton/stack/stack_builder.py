import requests

from account import Account
from stack.constants import Api, Operation, Queries




class StackBuilder:

    def __init__(self, class_ids):
        self.session = None
        self.class_ids = (
            [class_id for class_id in class_ids] if class_ids is not None else None
        )
        self._login()

    def _get_payload(self, operation, class_id=None):
        payload = {}
        variables = {}
        if operation == Operation.ADD:
            payload["operationName"] = "AddClassToStack"
            payload["query"] = Queries.ADD
            variables = {"input": {"pelotonClassId": class_id}}
        # todobison this doesn't work
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

    def _add_class(self, class_id):
        payload = self._get_payload(Operation.ADD, class_id)
        self.session.post(Api.ENDPOINT, json=payload)

    def _empty(self):
        payload = self._get_payload(Operation.EMPTY)
        resp = self.session.post(Api.ENDPOINT, json=payload)

    def _get(self):
        pass

    def _remove_class(self):
        pass

    def run(self):
        if self.class_ids is not None:
            for class_id in self.class_ids:
                self._add_class(class_id)
