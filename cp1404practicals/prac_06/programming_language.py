class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection="", year=0):
        self.name = name
        self.typing = typing.title()
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
