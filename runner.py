import requests
from pprint import pprint


class UserInput:
    DAYS = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    WEEKS = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"]

    def __init__(self):
        self.day = None
        self.week = None

    def _generate_prompt(self, question, options, add_newline=True):
        options = "\n".join(options)
        prompt = f"{question}\n{options}\nYour response: "
        if add_newline:
            prompt = "\n" + prompt
        return prompt

    def _week_prompt(self):
        question = "What week of the program is it?"
        options = [f"{indx + 1} = {week}" for indx, week in enumerate(self.WEEKS)]
        prompt = self._generate_prompt(question, options, add_newline=False)
        self.week = int(input(prompt))

    def _day_prompt(self):
        question = "What day of the week is it?"
        options = [f"{indx + 1} = {day}" for indx, day in enumerate(self.DAYS)]
        prompt = self._generate_prompt(question, options)
        self.day = int(input(prompt))

    def _confirm(self):
        day = self.format_time('day')
        week = self.format_time('week')
        question = (
            f"Programming Stack for {day}, {week}. Is this correct?"
        )
        options = ["1 - Yes", "2 - No"]
        prompt = self._generate_prompt(question, options)
        if input(prompt) == "2":
            print("Re-running...\n")
            self.run()

    def format_time(self, unit):
        if unit == "day":
            return self.DAYS[self.day - 1]
        elif unit == "week":
            return self.WEEKS[self.week - 1]

    def run(self):
        self._week_prompt()
        self._day_prompt()
        self._confirm()


ui = UserInput()
ui.run()


class Account:
    USERNAME = "bisonhubert@gmail.com"
    PASSWORD = "xxjM*RE_x4MPqPXmwGaU"


# Adrian Williams
class FullBodyStretchClass:
    DAY_1 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICJkZGM1MTlhZjMxMWU0ZTg3YmExNjY5Zjk3OTdhMjk0OSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    DAY_2 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICIxZTNjZWY3NGZkOTM0ZjdjYmM4NGY0MWFhZWZkNDQ2MiIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    DAY_3 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICIyYmYzOTIwMTUwZDQ0NDg1YjAyMmY3NTQ4YzIwZGI4NyIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    DAY_4 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICIxZjM3M2QxMWI4MWM0YWZlOGI2MjdmY2E2OTRhMjhlNSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    DAY_5 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICI4ZjgwZDZjZmFkMmI0YjEzOGE0NjljY2UxMDZmZWExOSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    DAY_6 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICI5N2RmMzdmYzkxMGE0ZWNmYjZkYjEwYzJiOTliNWI5OSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"
    DAY_7 = "eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICIxZGY4YTViZjEzZDY0YWMyOGEyMTk4ZjU5Y2JjY2Y1YSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"

    def get_class_id(self, day):
        if day == 1:
            return self.DAY_1
        elif day == 2:
            return self.DAY_2
        elif day == 3:
            return self.DAY_3
        elif day == 4:
            return self.DAY_4
        elif day == 5:
            return self.DAY_5
        elif day == 6:
            return self.DAY_6
        elif day == 7:
            return self.DAY_7

    def get_class_ids(self):
        return [
            self.DAY_1,
            self.DAY_2,
            self.DAY_3,
            self.DAY_4,
            self.DAY_5,
            self.DAY_6,
            self.DAY_7,
        ]


class Operation:
    ADD = "add"
    VIEW = "view"


class Stack:
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

    #
    # def _set_stack(self):
    #     payload = self._get_payload(Operation.VIEW)
    #     data = self.session.post(self.ENDPOINT, json=payload)
    #     import pdb;pdb.set_trace()
    #     self.stack = data.text
    #     return data
    #
    # def _print_stack(self):
    #     self._set_stack()
    #     pprint(self.stack)

    def run(self):
        self._login()
        if self.class_ids is not None:
            for class_id in self.class_ids:
                self._add_class(class_id)
        # todobison print stack
        # self._print_stack()


# full_body_stretch_classes = FullBodyStretchClass().get_class_ids()
# friday_class =
# stack = Stack([full_body_stretch_classes[-1]])
# stack.run()


# Questions
# 1. How to organize a class series (BYPZ, CYC, strength, custom) with IDs, instructor names, etc?


# Sample use case
# 1. Run runner.py
# 2. Asks week and day
# 3. Adds items for that to the stack (so the weeks and days have to be pre-computed)


# Day
# classes to add for a day of the week (M-Sun)

# Week
# series of days, can select a week number (1-4) and day number (1-7)

# Stack
# used to add classes to a stack or view the current
