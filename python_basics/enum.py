from enum import Enum

class Gander(Enum):
    MALE = 'M'
    FEMALE = 'F'


print(Gander.FEMALE)

for gander in Gander:
    print(gander)