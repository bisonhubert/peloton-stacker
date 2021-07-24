class Ride:

    def __init__(self, ride_token):
        self.token = ride_token

    def __str__(self):
        return f"ride={self.token}"
