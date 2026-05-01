import re
from datetime import datetime
from models.exceptions import FirstNameTooShortException, LastNameTooShortException, InvalidChessIDException, InvalidBirthDateException

class Player:
    def __init__(self, last_name, first_name, birth_date, chess_id):
        if len(last_name) < 2:
            raise LastNameTooShortException()
        if len(first_name) < 2:
            raise FirstNameTooShortException()
        try:
            datetime.strptime(birth_date, "%d/%m/%Y")
        except ValueError:
            raise InvalidBirthDateException()

        if not re.match(r"^[A-Z]{2}[0-9]{5}$", chess_id):
            raise InvalidChessIDException()
        
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.chess_id = chess_id

