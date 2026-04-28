from enum import Enum

class Role(Enum):
    LIBRARIAN = 1
    MEMBER = 2

class BookStatus(Enum):
    AVAILABLE = 1
    ISSUED = 2