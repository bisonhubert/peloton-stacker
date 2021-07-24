# todobison not sure I need this
class Instructor:
    def __init__(self, first_name, last_name, slug):
        self.first_name = first_name
        self.last_name = last_name
        self.slug = self.slug

    # format slug when initializing, forget the method to override atm

    def _format_slug(self):
        names = self.first_name.split(" ") + self.last_name.split(" ")
        return "-".join([name.lower() for name in names])

adrian_williams = Instructor('Adrian', 'Williams')
