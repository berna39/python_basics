from enum import Enum, unique

class Gander(Enum):
    MALE = 'M'
    FEMALE = 'F'


print(Gander.FEMALE)

for gander in Gander:
    print(gander)

#this will raise a value error
@unique
class MyEnum(Enum):
    ONE = 1
    TWO = 2
    THREE = 2

print(MyEnum.THREE)