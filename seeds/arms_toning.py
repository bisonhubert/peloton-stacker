from seeds.get_ride import GetRide

ARMS_TONING = {"operationName":"AddClassToStack","variables":{"input":{"pelotonClassId":"eyJob21lX3BlbG90b25faWQiOiBudWxsLCAicmlkZV9pZCI6ICI5MTE2ZTVmOTBjZmY0OGIzOTQ1MDVmMTI5OTM0ZDVmOCIsICJzdHVkaW9fcGVsb3Rvbl9pZCI6IG51bGwsICJ0eXBlIjogIm9uX2RlbWFuZCJ9"}},"query":"mutation AddClassToStack($input: AddClassToStackInput!) {\n  addClassToStack(input: $input) {\n    numClasses\n    totalTime\n    userStack {\n      stackedClassList {\n        playOrder\n        pelotonClass {\n          ...ClassDetails\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ClassDetails on PelotonClass {\n  joinToken\n  title\n  classId\n  fitnessDiscipline {\n    slug\n    __typename\n  }\n  assets {\n    thumbnailImage {\n      location\n      __typename\n    }\n    __typename\n  }\n  duration\n  ... on OnDemandInstructorClass {\n    title\n    fitnessDiscipline {\n      slug\n      displayName\n      __typename\n    }\n    contentFormat\n    difficultyLevel {\n      slug\n      displayName\n      __typename\n    }\n    airTime\n    instructor {\n      name\n      __typename\n    }\n    __typename\n  }\n  classTypes {\n    name\n    __typename\n  }\n  playableOnPlatform\n  __typename\n}\n"}

class ArmsToning(GetRide):
    DAY_1 = ARMS_TONING
    DAY_2 = None
    DAY_3 = ARMS_TONING
    DAY_4 = None
    DAY_5 = None
    DAY_6 = ARMS_TONING
    DAY_7 = None
