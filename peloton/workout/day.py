class Day:
    def __init__(self, number):
        self.number = number
        self.name = self._get_name_from_number(number)

    def _get_name_from_number(self, number):
        if type(number) != int:
            raise Exception(
                f"Property 'number' must be an integer. {self.number} is type {type(self.number)}"
            )
        if number < 1 or number > 7:
            raise Exception(
                f"Property 'number' represents day-of-week and cannot be less than 1 or greater than 7"
            )
        if number == 1:
            return "Monday"
        elif number == 2:
            return "Tuesday"
        elif number == 3:
            return "Wednesday"
        elif number == 4:
            return "Thursday"
        elif number == 5:
            return "Friday"
        elif number == 6:
            return "Saturday"
        elif number == 7:
            return "Sunday"

    def __str__(self):
        return f"name={self.name}"
