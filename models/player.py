import re
from datetime import datetime
from models.exceptions import FirstNameTooShortException, LastNameTooShortException, InvalidChessIDException, InvalidBirthDateException

class Player:
    last_id = 0
    @staticmethod
    def validate_last_name(last_name):
       if len(last_name) < 2:
            raise LastNameTooShortException(last_name)
       return last_name

    @staticmethod
    def validate_first_name(first_name):
        if len(first_name) < 2:
            raise FirstNameTooShortException(first_name)
        return first_name
    
    @staticmethod
    def validate_birth_date(birth_date):
        try:
            datetime.strptime(birth_date, "%d/%m/%Y")
            return birth_date
        
        except ValueError:
            raise InvalidBirthDateException()
        
    @staticmethod
    def validate_chess_id(chess_id):
        if chess_id == "":
            return chess_id
        if not re.match(r"^[A-Z]{2}[0-9]{5}$", chess_id):
            raise InvalidChessIDException()
        return chess_id



    def __init__(self, last_name, first_name, birth_date, chess_id):
         
        self.last_name = self.validate_last_name(last_name)
        self.first_name = self.validate_first_name(first_name)
        self.birth_date = self.validate_birth_date(birth_date)
        self.chess_id = self.validate_chess_id(chess_id)
        Player.last_id += 1
        self.player_id = Player.last_id

    def to_dict(self):
        """ Transforms the instance into a dictionary for JSON. """
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "chess_id": self.chess_id
        }
    
    @classmethod
    def from_dict(cls, data):
        """ Creates a Player instance from a dictionary. """
        return cls(**data)
    