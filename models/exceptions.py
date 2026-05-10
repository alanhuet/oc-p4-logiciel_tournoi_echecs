

class ChessProjectException(Exception):
    """Classe de base pour toutes nos exceptions."""
    pass

class LastNameTooShortException(ChessProjectException):
    def __init__(self, last_name=""):
        super().__init__(f"Le nom {last_name} est trop court ! (2 caractères minimum)")

class FirstNameTooShortException(ChessProjectException):
    def __init__(self, first_name=""):
        super().__init__(f"Le prénom {first_name} est trop court ! (2 caractères minimum)") 

class InvalidChessIDException(ChessProjectException):
    def __init__(self):
        super().__init__("L'identifiant national est invalide. Format attendu : AB12345")  

class InvalidBirthDateException(ChessProjectException):
    def __init__(self):
        super().__init__("Format de date invalide ! (Format attendu : JJ/MM/AAAA)")     

class TournamentNameTooShortException(ChessProjectException):
    def __init__(self, name=""):
        super().__init__(f"Le nom {name} est trop court ! (2 caractères minimum)")

class TournamentLocationTooShortException(ChessProjectException):
    def __init__(self, location=""):
        super().__init__(f"Le nom {location} est trop court ! (2 caractères minimum)") 

class InvalidStartDateException(ChessProjectException):
    def __init__(self):
        super().__init__("Format de date invalide ! (Format attendu : JJ/MM/AAAA)")

class InvalidEndDateException(ChessProjectException):
    def __init__(self):
        super().__init__("Format de date invalide ! (Format attendu : JJ/MM/AAAA)")      

class EndDateTooSoonException(ChessProjectException):
    def __init__(self):
        super().__init__("La date de fin du tournois ne peut être antérieure à la date du début.")                                