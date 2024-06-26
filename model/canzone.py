from dataclasses import dataclass

@dataclass
class Canzone:
    TrackId: int
    Name: str
    Bytes: int
    Milliseconds: int

    def __hash__(self):
        return hash(self.TrackId)

    def __str__(self):
        return f"{self.Name}"

    def __eq__(self, other):
        return self.TrackId == other.TrackId