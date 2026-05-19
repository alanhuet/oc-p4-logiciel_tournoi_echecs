
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
                
    def play_tournament(self):
        tournament = self.select_tournament()
        if not tournament:
            return
        
        while True:
            if tournament.current_round > tournament.rounds_count:
                self.view.show_error_message(f"Le tournoi '{tournament_name}' est terminé.")
                break

            round_in_progress = len(tournament.rounds) >= tournament.current_round

            choice = self.view.display_tournament_play_menu(
                tournament.name,
                tournament.current_round,
                round_in_progress
            )

            if choice == "1":
                if not round_in_progress:
                    self.start_next_round(tournament)
                else:
                    self.close_current_round(tournament)
            elif choice == "2":
                break
            else:
                self.view.show_error_message("Option invalide.")

    def start_next_round(self, tournament):
        """ Manages security and initiates the round. """
        # Security 1: even number of players
        if len(tournament.players) % 2 != 0:
            self.view.show_error_message(" Le nombre de joueurs doit être pair pour démarrer.")
            return
        
        # Security 2: Player/Round Ratio
        if len(tournament.players) < (tournament.rounds_count * 2):
            self.view.show_error_message(f"Il faut au moins {tournament.rounds_count * 2} joueurs inscrit au tournoi.")
            return
        
        from models.round import Round
        round_name = f"round {tournament.current_round}"
        matches = []

        if tournament.current_round == 1:
            # random player mix
            import random
            shuffled_players = tournament.players[:]
            random.shuffle(shuffled_players)

            for i in range(0, len(shuffled_players), 2):
                match = ([shuffled_players[i], 0.0], [shuffled_players[i+1], 0.0])
                matches.append(match)

        else:
            # Les rounds suivants seront codés ici plus tard
            ...

        new_round = Round(name=round_name, matches=matches)
        tournament.rounds.append(new_round)
        self.save_all_tournaments()

        self.view.display_round_pairings(new_round.name, new_round.matches)

    def close_current_round(self, tournament):
        """ Manages data entry, score validation, and progression to the next round. """
        current_round_obj = tournament.rounds[-1]

        while True:
            # score entry
            for i, (p1_data, p2_data) in enumerate(current_round_obj.matches, 1):
                s1, s2 = self.view.prompt_for_match_score(i, p1_data[0], p2_data[0])
                p1_data[1] = s1
                p2_data[1] = s2

            # Request for validation of the summary
            if self.view.display_round_summary(current_round_obj.matches):
                current_round_obj.mark_as_completed()
                tournament.current_round += 1
                self.save_all_tournaments()
                print(f"\n[SUCCCÈS] {current_round_obj.name} clôturé. Passage au round {tournament.current_round}.")
                break
            else:
                print("\n[INFO] Retour à la saisie des scores.")



