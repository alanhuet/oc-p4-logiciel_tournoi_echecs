
from models.tournament import Tournament
from views.tournament_view import TournamentView
from models.storage import StorageManager
from models.exceptions import ChessProjectException
from models.player import Player

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

    def select_tournament(self):
        if not self.tournaments:
            self.view.show_error_message("Aucun tournoi enregistré.")
            return None
        
        print("\n---SÉLECTION DU TOURNOI---")
        for t in self.tournaments:
            print(f"ID: {t.tournament_id} | {t.name} ({t.location}) - {len(t.players)} joueurs inscrits.")

        choice = input("\nEntrez l'ID du tournoi : ")
        try:
            target_id = int(choice)

            selected_tournament = next((t for t in self.tournaments if t.tournament_id == target_id), None)

            if selected_tournament:
                return selected_tournament
            else:
                self.view.show_error_message(f"Aucun tournoi ne possède l'ID {target_id}.")
                return None
        except ValueError:
            self.view.show_error_message("Veuillez entrer un identifiant numérique valide.")
            return None
        
    def manage_tournament_participants(self):
        tournament = self.select_tournament()
        if not tournament:
            return
        
        player_storage = StorageManager("players")
        player_data = player_storage.load()
        available_players = [Player.from_dict(p) for p in player_data]

        if not available_players:
            self.view.show_error_message("Aucun joueur enregistré dans la base de données.")
            return
        available_players = sorted(available_players, key=lambda p: p.last_name.lower())
        while True:
            self.view.display_available_players(available_players)
            choice = self.view.prompt_for_player_number()

            if choice.lower() == 'q':
                break
            try:
                target_id = int(choice)
                selected_player = next((p for p in available_players if p.player_id == target_id), None)
                if selected_player is not None:

                    if any (p.player_id == selected_player.player_id for p in tournament.players):
                        self.view.show_error_message(f"{selected_player.last_name.upper()} est déjà inscrit à ce tournoi.")
                    else:
                        tournament.players.append(selected_player)
                        self.view.show_player_added_to_tournament(
                            f"{selected_player.first_name} {selected_player.last_name.upper()}",
                            tournament.name
                        )
                        self.save_all_tournaments()
                else:
                    self.view.show_error_message(f"Aucun joueur ne possède l'ID {target_id}.")
            except ValueError:
                self.view.show_error_message("saisie Invalide. Entrez un ID numérique ou 'q' pour quitter.")                
                
    
