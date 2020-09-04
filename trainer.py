"""Import Pikachu."""

from pikachu import Pikachu


class Trainer():
    """Create class Trainer."""

    def __init__(self, name):
        """Initialize Team properties."""
        self._name = name
        self.pokemon = Pikachu('puppy', 'Water', 'woof', 'sailor cap')

    def speak(self):
        """Write speak method."""
        return f'My name is {self._name} and my pokemon is {self.pokemon.nickname}.'
