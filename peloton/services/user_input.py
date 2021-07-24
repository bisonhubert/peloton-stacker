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
        day = self.format_time("day")
        week = self.format_time("week")
        question = f"Programming Stack for {day}, {week}. Is this correct?"
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
