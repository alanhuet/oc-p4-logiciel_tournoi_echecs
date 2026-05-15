
from datetime import datetime
from models.exceptions import TournamentNameTooShortException, TournamentLocationTooShortException, InvalidDateException, EndDateTooSoonException

class Round:
    def __init__(self, name, matches=None):
        self.name = name
        self.start_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.end_time = None
        self.matches = matches if matches else []

    def close_round(self):
        self.end_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def to_dict(self):
        return {
            "name": self.name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "matches": self.matches
        }
    
    @classmethod
    def from_dict(cls, data):
        round_inst = cls(data["name"], data["matches"])
        round_inst.start_time = data["start_time"]
        round_inst.end_time = data["end_time"]
        return round_inst
    
class Tournament:
    last_id = 0

    @staticmethod
    def validate_tournament_name(name):
        if len(name) < 2:
            raise TournamentNameTooShortException(name)
        return name
        
    @staticmethod
    def validate_tournament_location(location):
        if len(location) < 2:
            raise TournamentLocationTooShortException(location)
        return location
    
    @staticmethod
    def validate_start_date(start_date):
        try:
            datetime.strptime(start_date, "%d/%m/%Y")
            return start_date
        except ValueError:
            raise InvalidDateException()
        
    @staticmethod
    def validate_end_date(end_date):
        try:
            datetime.strptime(end_date, "%d/%m/%Y")
            return end_date
        except ValueError:
            raise InvalidDateException()    
        
    @staticmethod
    def validate_tournament_dates(start_date, end_date):
        s_date = datetime.strptime(start_date, "%d/%m/%Y")
        e_date = datetime.strptime(end_date, "%d/%m/%Y")

        if e_date < s_date:
            raise EndDateTooSoonException()
        return True    
            
    def __init__(self, name, location, start_date, end_date, description, rounds_count=4, tournament_id=None):
        self.name = self.validate_tournament_name(name)
        self.location = self.validate_tournament_location(location)
        self.start_date = self.validate_start_date(start_date)
        self.end_date = self.validate_end_date(end_date)
        self.validate_tournament_dates(self.start_date, self.end_date)
        self.description = description
        self.rounds_count = rounds_count
        self.current_round = 1
        self.players = []
        self.rounds = []

        Tournament.last_id += 1
        if tournament_id:
            self.tournament_id = tournament_id
        else:
            self.tournament_id = Tournament.last_id

    def to_dict(self):
        return {
            "tournament_id": self.tournament_id,
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "rounds_count": self.rounds_count,
            "current_round": self.current_round,
            "players": [p.to_dict() for p in self.players],
            "rounds": [r.to_dict() for r in self.rounds]
        }
    
    @classmethod
    def from_dict(cls, data):
        player_data = data.pop("players", [])
        rounds_data = data.pop("rounds", [])
        current_round = data.pop("current_round", 1)

        tournament = cls(**data)
        tournament.current_round = current_round

        from models.player import Player
        tournament.players = [Player.from_dict(p) for p in player_data]
        tournament.rounds = [Round.from_dict(r) for r in rounds_data]

        return tournament