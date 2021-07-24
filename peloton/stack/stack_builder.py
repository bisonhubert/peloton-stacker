import requests

from account import Account


class Operation:
    ADD = "add"
    VIEW = "view"


class StackBuilder:
    ENDPOINT = "https://gql-graphql-gateway.prod.k8s.onepeloton.com/graphql"
    GET_QUERY = "query ViewUserStack {  viewUserStack {    numClasses    totalTime    ... on StackResponseSuccess {      numClasses      totalTime      userStack {        stackedClassList {          playOrder          pelotonClass {            joinToken            title            classId            fitnessDiscipline {              slug              __typename            }            assets {              thumbnailImage {                location                __typename              }              __typename            }            duration            ... on OnDemandInstructorClass {              joinToken              title              fitnessDiscipline {                slug                displayName                __typename              }              contentFormat              totalUserWorkouts              originLocale {                language                __typename              }              captions {                locales                __typename              }              timeline {                startOffset                __typename              }              difficultyLevel {                slug                displayName                __typename              }              airTime              instructor {                name                __typename              }              __typename            }            classTypes {              name              __typename            }            playableOnPlatform            __typename          }          __typename        }        __typename      }      __typename    }    __typename  }}"
    POST_QUERY = "mutation AddClassToStack($input: AddClassToStackInput!) {\n addClassToStack(input: $input) {\n numClasses\n totalTime\n userStack {\n stackedClassList {\n playOrder\n pelotonClass {\n ...ClassDetails\n __typename\n }\n __typename\n }\n __typename\n }\n __typename\n }\n}\n\nfragment ClassDetails on PelotonClass {\n joinToken\n title\n classId\n fitnessDiscipline {\n slug\n __typename\n }\n assets {\n thumbnailImage {\n location\n __typename\n }\n __typename\n }\n duration\n ... on OnDemandInstructorClass {\n title\n fitnessDiscipline {\n slug\n displayName\n __typename\n }\n contentFormat\n difficultyLevel {\n slug\n displayName\n __typename\n }\n airTime\n instructor {\n name\n __typename\n }\n __typename\n }\n classTypes {\n name\n __typename\n }\n playableOnPlatform\n __typename\n}\n"

    def __init__(self, class_ids):
        self.session = None
        self.class_ids = (
            [class_id for class_id in class_ids] if class_ids is not None else None
        )

    def _get_payload(self, operation, class_id=None):
        payload = {}
        variables = {}
        if operation == Operation.ADD:
            payload["operationName"] = "AddClassToStack"
            payload["query"] = self.POST_QUERY
            variables = {"input": {"pelotonClassId": class_id}}
        elif operation == Operation.VIEW:
            payload["operationName"] = "ViewUserStack"
            payload["query"] = self.GET_QUERY
        payload["variables"] = variables
        return payload

    def _login(self):
        s = requests.Session()
        payload = {"username_or_email": Account.USERNAME, "password": Account.PASSWORD}
        s.post("https://api.onepeloton.com/auth/login", json=payload)
        self.session = s

    def _add_class(self, class_id):
        payload = self._get_payload(Operation.ADD, class_id)
        self.session.post(self.ENDPOINT, json=payload)

    def _get(self):
        pass

    def _remove_class(self):
        pass

    def run(self):
        self._login()
        if self.class_ids is not None:
            for class_id in self.class_ids:
                self._add_class(class_id)
