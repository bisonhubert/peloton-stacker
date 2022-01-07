from seeds.get_ride import GetRide

DAY_4 = None
# uncomment to add a cool down. generally, thursdays (day 4) are low impact
# DAY_4 = {"operationName":"AddClassToStack","variables":{"input":{"pelotonClassId":"eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICI3YjlhNzY1MDIzMWM0NmExOTViZmEzOTBiY2FjZjMyYiIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"}},"query":"mutation AddClassToStack($input: AddClassToStackInput!) {\n  addClassToStack(input: $input) {\n    numClasses\n    totalTime\n    userStack {\n      stackedClassList {\n        playOrder\n        pelotonClass {\n          ...ClassDetails\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ClassDetails on PelotonClass {\n  joinToken\n  title\n  classId\n  fitnessDiscipline {\n    slug\n    __typename\n  }\n  assets {\n    thumbnailImage {\n      location\n      __typename\n    }\n    __typename\n  }\n  duration\n  ... on OnDemandInstructorClass {\n    title\n    fitnessDiscipline {\n      slug\n      displayName\n      __typename\n    }\n    contentFormat\n    difficultyLevel {\n      slug\n      displayName\n      __typename\n    }\n    airTime\n    instructor {\n      name\n      __typename\n    }\n    __typename\n  }\n  classTypes {\n    name\n    __typename\n  }\n  playableOnPlatform\n  __typename\n}\n"}

class CoolDown(GetRide):
    DAY_1 = {"operationName":"AddClassToStack","variables":{"input":{"pelotonClassId":"eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICIzMDg3NGViNjVmMDU0ZmIyYTNiMzZhMzRjOGQ1MWNjOCIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"}},"query":"mutation AddClassToStack($input: AddClassToStackInput!) {\n  addClassToStack(input: $input) {\n    numClasses\n    totalTime\n    userStack {\n      stackedClassList {\n        playOrder\n        pelotonClass {\n          ...ClassDetails\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ClassDetails on PelotonClass {\n  joinToken\n  title\n  classId\n  fitnessDiscipline {\n    slug\n    __typename\n  }\n  assets {\n    thumbnailImage {\n      location\n      __typename\n    }\n    __typename\n  }\n  duration\n  ... on OnDemandInstructorClass {\n    title\n    fitnessDiscipline {\n      slug\n      displayName\n      __typename\n    }\n    contentFormat\n    difficultyLevel {\n      slug\n      displayName\n      __typename\n    }\n    airTime\n    instructor {\n      name\n      __typename\n    }\n    __typename\n  }\n  classTypes {\n    name\n    __typename\n  }\n  playableOnPlatform\n  __typename\n}\n"}
    DAY_2 = {"operationName":"AddClassToStack","variables":{"input":{"pelotonClassId":"eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICJiZTJhMTk3ZDk0ZTQ0YTZmODA2ZDdmNmUwM2YxNGIzZSIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"}},"query":"mutation AddClassToStack($input: AddClassToStackInput!) {\n  addClassToStack(input: $input) {\n    numClasses\n    totalTime\n    userStack {\n      stackedClassList {\n        playOrder\n        pelotonClass {\n          ...ClassDetails\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ClassDetails on PelotonClass {\n  joinToken\n  title\n  classId\n  fitnessDiscipline {\n    slug\n    __typename\n  }\n  assets {\n    thumbnailImage {\n      location\n      __typename\n    }\n    __typename\n  }\n  duration\n  ... on OnDemandInstructorClass {\n    title\n    fitnessDiscipline {\n      slug\n      displayName\n      __typename\n    }\n    contentFormat\n    difficultyLevel {\n      slug\n      displayName\n      __typename\n    }\n    airTime\n    instructor {\n      name\n      __typename\n    }\n    __typename\n  }\n  classTypes {\n    name\n    __typename\n  }\n  playableOnPlatform\n  __typename\n}\n"}
    DAY_3 = {"operationName":"AddClassToStack","variables":{"input":{"pelotonClassId":"eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICJmZTdhMmNkZWU2Nzg0NGEzYTg4NWEzYTk1ZWEwOWE2NiIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"}},"query":"mutation AddClassToStack($input: AddClassToStackInput!) {\n  addClassToStack(input: $input) {\n    numClasses\n    totalTime\n    userStack {\n      stackedClassList {\n        playOrder\n        pelotonClass {\n          ...ClassDetails\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ClassDetails on PelotonClass {\n  joinToken\n  title\n  classId\n  fitnessDiscipline {\n    slug\n    __typename\n  }\n  assets {\n    thumbnailImage {\n      location\n      __typename\n    }\n    __typename\n  }\n  duration\n  ... on OnDemandInstructorClass {\n    title\n    fitnessDiscipline {\n      slug\n      displayName\n      __typename\n    }\n    contentFormat\n    difficultyLevel {\n      slug\n      displayName\n      __typename\n    }\n    airTime\n    instructor {\n      name\n      __typename\n    }\n    __typename\n  }\n  classTypes {\n    name\n    __typename\n  }\n  playableOnPlatform\n  __typename\n}\n"}
    DAY_4 = {"operationName":"AddClassToStack","variables":{"input":{"pelotonClassId":"eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICJjZjgyMGM3NzZiMmM0YzA5ODllZGU4MmIzYjQ1YmI5NiIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"}},"query":"mutation AddClassToStack($input: AddClassToStackInput!) {\n  addClassToStack(input: $input) {\n    numClasses\n    totalTime\n    userStack {\n      stackedClassList {\n        playOrder\n        pelotonClass {\n          ...ClassDetails\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ClassDetails on PelotonClass {\n  joinToken\n  title\n  classId\n  fitnessDiscipline {\n    slug\n    __typename\n  }\n  assets {\n    thumbnailImage {\n      location\n      __typename\n    }\n    __typename\n  }\n  duration\n  ... on OnDemandInstructorClass {\n    title\n    fitnessDiscipline {\n      slug\n      displayName\n      __typename\n    }\n    contentFormat\n    difficultyLevel {\n      slug\n      displayName\n      __typename\n    }\n    airTime\n    instructor {\n      name\n      __typename\n    }\n    __typename\n  }\n  classTypes {\n    name\n    __typename\n  }\n  playableOnPlatform\n  __typename\n}\n"}
    DAY_5 = {"operationName":"AddClassToStack","variables":{"input":{"pelotonClassId":"eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICI2MjMzODRlNjk3ZDI0ZmNkOGZlOWNmYmIzNDA2ZWEwOCIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"}},"query":"mutation AddClassToStack($input: AddClassToStackInput!) {\n  addClassToStack(input: $input) {\n    numClasses\n    totalTime\n    userStack {\n      stackedClassList {\n        playOrder\n        pelotonClass {\n          ...ClassDetails\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ClassDetails on PelotonClass {\n  joinToken\n  title\n  classId\n  fitnessDiscipline {\n    slug\n    __typename\n  }\n  assets {\n    thumbnailImage {\n      location\n      __typename\n    }\n    __typename\n  }\n  duration\n  ... on OnDemandInstructorClass {\n    title\n    fitnessDiscipline {\n      slug\n      displayName\n      __typename\n    }\n    contentFormat\n    difficultyLevel {\n      slug\n      displayName\n      __typename\n    }\n    airTime\n    instructor {\n      name\n      __typename\n    }\n    __typename\n  }\n  classTypes {\n    name\n    __typename\n  }\n  playableOnPlatform\n  __typename\n}\n"}
    DAY_6 = {"operationName":"AddClassToStack","variables":{"input":{"pelotonClassId":"eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICJmNTlkOTFmOWY1NDY0ZWRlYTVkMjM1NzFlM2NjMjM3NCIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"}},"query":"mutation AddClassToStack($input: AddClassToStackInput!) {\n  addClassToStack(input: $input) {\n    numClasses\n    totalTime\n    userStack {\n      stackedClassList {\n        playOrder\n        pelotonClass {\n          ...ClassDetails\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ClassDetails on PelotonClass {\n  joinToken\n  title\n  classId\n  fitnessDiscipline {\n    slug\n    __typename\n  }\n  assets {\n    thumbnailImage {\n      location\n      __typename\n    }\n    __typename\n  }\n  duration\n  ... on OnDemandInstructorClass {\n    title\n    fitnessDiscipline {\n      slug\n      displayName\n      __typename\n    }\n    contentFormat\n    difficultyLevel {\n      slug\n      displayName\n      __typename\n    }\n    airTime\n    instructor {\n      name\n      __typename\n    }\n    __typename\n  }\n  classTypes {\n    name\n    __typename\n  }\n  playableOnPlatform\n  __typename\n}\n"}
    DAY_7 = {"operationName":"AddClassToStack","variables":{"input":{"pelotonClassId":"eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICJkM2JkNGEyNWE3ZmY0OTMyOTg3MTlhYjhjMDU5ZDNlNiIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"}},"query":"mutation AddClassToStack($input: AddClassToStackInput!) {\n  addClassToStack(input: $input) {\n    numClasses\n    totalTime\n    userStack {\n      stackedClassList {\n        playOrder\n        pelotonClass {\n          ...ClassDetails\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ClassDetails on PelotonClass {\n  joinToken\n  title\n  classId\n  fitnessDiscipline {\n    slug\n    __typename\n  }\n  assets {\n    thumbnailImage {\n      location\n      __typename\n    }\n    __typename\n  }\n  duration\n  ... on OnDemandInstructorClass {\n    title\n    fitnessDiscipline {\n      slug\n      displayName\n      __typename\n    }\n    contentFormat\n    difficultyLevel {\n      slug\n      displayName\n      __typename\n    }\n    airTime\n    instructor {\n      name\n      __typename\n    }\n    __typename\n  }\n  classTypes {\n    name\n    __typename\n  }\n  playableOnPlatform\n  __typename\n}\n"}
