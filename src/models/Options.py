from enum import Enum


class MainOption(Enum):
    List = 1
    Add = 2
    Remove = 3
    Sort = 4
    Exit = 5


class RemoveOption(Enum):
    Name = 1
    PhoneNumber = 2
    Email = 3
