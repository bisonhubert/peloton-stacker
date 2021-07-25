class Ride:

    def __init__(self, slug=None, token=None):
        self.slug = slug
        self.token = token

    def __str__(self):
        return f"ride={self.token}"
