class Api:
    ENDPOINT = "https://gql-graphql-gateway.prod.k8s.onepeloton.com/graphql"


class Operation:
    ADD = "add"
    EMPTY = "empty"
    VIEW = "view"


class Queries:
    ADD = "mutation AddClassToStack($input: AddClassToStackInput!) {\n addClassToStack(input: $input) {\n numClasses\n totalTime\n userStack {\n stackedClassList {\n playOrder\n pelotonClass {\n ...ClassDetails\n __typename\n }\n __typename\n }\n __typename\n }\n __typename\n }\n}\n\nfragment ClassDetails on PelotonClass {\n joinToken\n title\n classId\n fitnessDiscipline {\n slug\n __typename\n }\n assets {\n thumbnailImage {\n location\n __typename\n }\n __typename\n }\n duration\n ... on OnDemandInstructorClass {\n title\n fitnessDiscipline {\n slug\n displayName\n __typename\n }\n contentFormat\n difficultyLevel {\n slug\n displayName\n __typename\n }\n airTime\n instructor {\n name\n __typename\n }\n __typename\n }\n classTypes {\n name\n __typename\n }\n playableOnPlatform\n __typename\n}\n"
    CLEAR = "mutation ModifyStack($input: ModifyStackInput!) {\n modifyStack(input: $input) {\n numClasses\n totalTime\n userStack {\n stackedClassList {\n playOrder\n pelotonClass {\n ...ClassDetails\n __typename\n }\n __typename\n }\n __typename\n }\n __typename\n }\n}\n\nfragment ClassDetails on PelotonClass {\n joinToken\n title\n classId\n fitnessDiscipline {\n slug\n __typename\n }\n assets {\n thumbnailImage {\n location\n __typename\n }\n __typename\n }\n duration\n ... on OnDemandInstructorClass {\n title\n fitnessDiscipline {\n slug\n displayName\n __typename\n }\n contentFormat\n difficultyLevel {\n slug\n displayName\n __typename\n }\n airTime\n instructor {\n name\n __typename\n }\n __typename\n }\n classTypes {\n name\n __typename\n }\n playableOnPlatform\n __typename\n}\n"
    GET = "query ViewUserStack {\n viewUserStack {\n numClasses\n totalTime\n ... on StackResponseSuccess {\n numClasses\n totalTime\n userStack {\n stackedClassList {\n playOrder\n pelotonClass {\n joinToken\n title\n classId\n fitnessDiscipline {\n slug\n __typename\n }\n assets {\n thumbnailImage {\n location\n __typename\n … slug\n displayName\n __typename\n }\n airTime\n instructor {\n name\n __typename\n }\n __typename\n }\n classTypes {\n name\n __typename\n }\n playableOnPlatform\n __typename\n }\n __typename\n }\n __typename\n }\n __typename\n }\n __typename\n }\n}\n"
