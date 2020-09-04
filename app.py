"""Import classes from modules."""


from pokemon import Pokemon
from pikachu import Pikachu
from trainer import Trainer


turtleoid = Pokemon('turt', 'Water', 'spray')
print(turtleoid.speak())

pika = Pikachu('Pika', 'Electric', 'zap', 'birthday hat')
print(pika.speak())

ash = Trainer('Ash')
print(ash.speak())
