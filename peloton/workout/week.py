class Week:

    def __init__(self, number, days=None):
        if number < 1 or number > 5:
            raise Exception(
                f"Property 'number' represents week of month and cannot be less than 1 or greater than 5"
            )
        if type(number) != int:
            raise Exception(
                f"Property 'number' must be an integer. {self.number} is type {type(self.number)}"
            )
        self.number = number
        self.days = [day for day in days] if days is not None else None

    def __str__(self):
        return f"week={self.number}"
