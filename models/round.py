from datetime import datetime

class Round:
    def __init__(self, name, matches=None):
        self.name = name
        self.matches = matches if matches is not None else []
        self.start_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.end_time = None

    def mark_as_completed(self):
        """ Freezes the round end time. """
        self.end_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def to_dict(self):
        """ Convert to dictionary for JSON file. """
        return {
            "name": self.name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "matches": [
                ([p1.to_dict(), s1], [p2.to_dict(), s2])
                for (p1, s1), (p2, s2) in self.matches
            ]

        }
    
    @classmethod
    def from_dict(cls, data):
        """ Rebuild from dictionary from JSON file. """
        from models.player import Player
        instance = cls(name=data["name"])
        instance.start_time = data["start_time"]
        instance.end_time = data["end_time"]
        instance.matches = [
            ([Player.from_dict(p1), s1], [Player.from_dict(p2), s2])
            for (p1, s1), (p2, s2) in data["matches"]
        ]
        return instance