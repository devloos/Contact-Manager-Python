import enum


class MainMenu(enum):
    List = 1
    Add = 2
    Remove = 3
    Exit = 4


class RemoveMenu(enum):
    Name = 1
    PhoneNumber = 2
    Email = 3


class SortMenu(enum):
    Name = 1
    Email = 2
    Relationship = 3
