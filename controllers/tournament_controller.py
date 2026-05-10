
from models.tournament import Tournament
from views.tournament_view import TournamentView
from models.storage import StorageManager
from models.exceptions import ChessProjectException

class TournamentController:
    def __init__(self):
        self.view = TournamentView()
        self.storage = StorageManager("tournaments")

        # Le from_dict devra être complété plus tard pour les objets internes
        self.tournaments = [Tournament.from_dict(t) for t in self.storage.load()]

    def create_tournament(self):
        data = self.view.prompt_for_tournament_data()

        if data.get("rounds_count") is None:
            data.pop("rounds_count")

        try:
            new_tournament = Tournament(**data)
            
            self.tournaments.append(new_tournament)
            self.save_all_tournaments()

            self.view.show_tournament_created_success(new_tournament.name)
            return new_tournament
        except ChessProjectException as error:
            self.view.show_error_message(str(error))
            return None
        
    def save_all_tournaments(self):
        data_to_save = [t.to_dict() for t in self.tournaments]
        self.storage.save(data_to_save)
