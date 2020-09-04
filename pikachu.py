"""Import super class."""

from pokemon import Pokemon

class Pikachu(Pokemon):
    def __init__(self, nickname, type, moves, hat):
        super().__init__(nickname, type, moves)
        self.hat = hat

    def speak(self):
        """Override Pokemon speak method."""
        return f'They call me {self.nickname} and I am wearing a {self.hat}.'
