from dataclasses import dataclass
from datetime import datetime


@dataclass
class Avvistamento:
    id: int
    data: datetime
    stato: str
    citta: str


    def __hash__(self): # stringa lunga uguale
        return hash(self.id)

    def __str__(self):
        return f"id: {self.id} - {self.citta} [{self.stato}], {self.data}"