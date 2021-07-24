from graphql_ids import AdrianWilliams

class Ride:

    def __init__(self, graphql_id, instructor_slug):
        self.graphql_id = graphql_id
        self.instructor_slug = instructor_slug
        # some of below can be filled out with a getter from the website using the ID
        # others are future features
            # - name
            # - duration
            # - slug
            # - next classes (list of slugs, op)
            # - instructor (slug)
            # - id (from website)
            # - tags (list, for filtering)
            # - times taken
