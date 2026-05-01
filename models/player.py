import re
from datetime import datetime
from models.exceptions import FirstNameTooShortException, LastNameTooShortException, InvalidChessIDException, InvalidBirthDateException

class Player:
    @staticmethod
    def validate_last_name(last_name):
       if len(last_name) < 2:
            raise LastNameTooShortException()
       return last_name

    @staticmethod
    def validate_first_name(first_name):
        if len(first_name) < 2:
            raise FirstNameTooShortException()
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
         if not re.match(r"^[A-Z]{2}[0-9]{5}$", chess_id):
            raise InvalidChessIDException()
         return chess_id



    def __init__(self, last_name, first_name, birth_date, chess_id):
         
        self.last_name = self.validate_last_name(last_name)
        self.first_name = self.validate_first_name(first_name)
        self.birth_date = self.validate_birth_date(birth_date)
        self.chess_id = self.validate_chess_id(chess_id)

