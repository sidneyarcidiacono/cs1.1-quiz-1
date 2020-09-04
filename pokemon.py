class Pokemon:
    """Define Pokemon class."""

    def __init__(self, nickname, type, moves):
        """Initialize Pokemon properties."""
        self.nickname = nickname
        self.type = type
        self.moves = moves


    def speak(self):
        return f'My nickname is {self.nickname} and my type is {self.type}.'
