from enum import Enum


class MainOption(Enum):
    List = 1
    Add = 2
    Remove = 3
    Exit = 4


class RemoveOption(Enum):
    Name = 1
    PhoneNumber = 2
    Email = 3


class SortOption(Enum):
    Name = 1
    Email = 2
    Relationship = 3
