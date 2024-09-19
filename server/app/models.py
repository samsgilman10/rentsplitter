from redis_om import HashModel, JsonModel
from typing import List, Tuple

class Room(HashModel):
    label: str

class Person(HashModel):
    name: str

class ChoiceSet(JsonModel):
    prices: List[Tuple[Room, int]]
    choices: List[Tuple[Person, Room]]

class Session(JsonModel):
    code: str
    rooms: List[Room]
    roommates: List[Person]
    bids: List[ChoiceSet]
