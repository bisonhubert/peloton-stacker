import base64
import json
import os
from urllib.parse import parse_qs, urlparse

import requests

from stack.constants import Api, Queries


def class_id_from(value):
    query = parse_qs(urlparse(value).query)
    if "classId" in query:
        return query["classId"][0]
    return value


def search_params_from(url):
    params = {}
    for key, values in parse_qs(urlparse(url).query).items():
        value = values[0]
        if value.startswith("["):
            value = ",".join(json.loads(value))
        params[Api.SEARCH_PARAM_NAMES.get(key, key)] = value
    return params


class Client:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers["Peloton-Platform"] = "web"
        self._login()

    def _login(self):
        payload = {
            "grant_type": "password",
            "client_id": Api.CLIENT_ID,
            "scope": "offline_access openid",
            "username": os.environ["PELOTON_USERNAME"],
            "password": os.environ["PELOTON_PASSWORD"],
        }
        resp = requests.post(Api.TOKEN_URL, json=payload, timeout=10)
        resp.raise_for_status()
        self.session.headers["Authorization"] = f"Bearer {resp.json()['access_token']}"

    @staticmethod
    def _join_token(class_id):
        ride = {
            "home_peloton_id": None,
            "ride_id": class_id,
            "studio_peloton_id": None,
            "type": "on_demand",
        }
        return base64.b64encode(json.dumps(ride).encode()).decode()

    def _graphql(self, operation, query, variables):
        payload = {"operationName": operation, "query": query, "variables": variables}
        resp = self.session.post(Api.ENDPOINT, json=payload, timeout=10)
        resp.raise_for_status()
        body = resp.json()
        if body.get("errors"):
            raise RuntimeError(body["errors"])
        return body["data"]

    def add_class(self, class_id):
        variables = {"input": {"pelotonClassId": self._join_token(class_id)}}
        return self._graphql("AddClassToStack", Queries.ADD, variables)["addClassToStack"]

    def empty_stack(self):
        variables = {"input": {"pelotonClassIdList": []}}
        return self._graphql("ModifyStack", Queries.CLEAR, variables)["modifyStack"]

    def _get(self, url, params=None):
        resp = self.session.get(url, params=params, timeout=10)
        resp.raise_for_status()
        return resp.json()

    def ride(self, class_id):
        return self._get(Api.RIDE_URL.format(class_id))["ride"]

    def instructor_names(self):
        data = self._get(Api.INSTRUCTORS_URL, {"limit": 500})["data"]
        return {i["id"]: i["name"] for i in data}

    def search_classes(self, params, limit):
        return self._get(Api.SEARCH_URL, {**params, "limit": limit, "page": 0})["data"]
