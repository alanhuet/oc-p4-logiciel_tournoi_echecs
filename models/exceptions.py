

class ChessProjectException(Exception):
    """Classe de base pour toutes nos exceptions."""
    pass

class LastNameTooShortException(ChessProjectException):
    def __init__(self, last_name="Le nom"):
        super().__init__(f"{last_name} est trop court ! (2 caractères minimum)")

class FirstNameTooShortException(ChessProjectException):
    def __init__(self, first_name="Le prénom"):
        super().__init__(f"{first_name} est trop court ! (2 caractères minimum)") 

class InvalidChessIDException(ChessProjectException):
    def __init__(self):
        super().__init__("L'identifiant national est invalide. Format attendu : AB12345")  

class InvalidBirthDateException(ChessProjectException):
    def __init__(self):
        super().__init__("Format de date invalide ! (Format attendu : JJ/MM/AAAA)")     