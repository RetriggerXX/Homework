from dataclasses import dataclass

@dataclass
class Book:
   id: int
   title: str
   autor: str
   year: int
   status: int
@dataclass
class Reader:
    id: int
    name: str
    age: int


