from models.tournament import Tournament

class TournamentView:
    def prompt_for_tournament_data(self):
        print("\n" + "-"*10 + "CRÉATION DU TOURNOI" + "-"*10)

        while True:
            name = input("Nom du tournoi : ")
            try:
                Tournament.validate_tournament_name(name)
                break
            except Exception as e:
                self.show_error_message(e)

        while True:
            location = input("Lieu : ")
            try:
                Tournament.validate_tournament_location(location)
                break
            except Exception as e:
                self.show_error_message(e)

        while True:
            start_date = input("Date de début (JJ/MM/AAAA): ")
            try:
                Tournament.validate_start_date(start_date)
                break
            except Exception as e:
                self.show_error_message(e)

        while True:
            end_date = input("Date de fin (JJ/MM/AAAA): ")
            try:
                Tournament.validate_end_date(end_date)
                Tournament.validate_tournament_dates(start_date, end_date)
                break
            except Exception as e:
                self.show_error_message(e)

        description = input("Descritpion / Remarques : ")

        rounds_count = input("Nombre de tours (appuyez sur Entrée por 4) : ")
        if rounds_count.isdigit():
            rounds_count = int(rounds_count)
        else:
            rounds_count = None

        return {
            "name": name,
            "location": location,
            "start_date": start_date,
            "end_date": end_date,
            "description": description,
            "rounds_count": rounds_count
        }
    
    def show_tournament_created_success(self, name):
        print(f"\n[SUCCES] Le tournoi {name} a été créé.")

    def show_error_message(self, message):
        print(f"\n[ERREUR] {message}")  

    def display_available_players(self, players):
        print("\n" + "-" * 13 + " JOUEURS DISPONIBLES " + "-" * 13)
        print(f"{'NOM':<15} | {'PRÉNOM':<15} | {'ID':<5}")
        print("-" * 43)

        for p in players:
            print(f"{p.last_name.upper():<15} | {p.first_name.capitalize():<15} | {p.player_id:<5}")

        print("-"*43)

    def prompt_for_player_number(self):
        return input("Entrez l'ID du joueur à inscire (ou 'q' pour quitter) :")
    
    def show_player_added_to_tournament(self, player_name, tournament_name):
        print(f"\n[SUCCÈS] {player_name} a été inscrit au tournoi '{tournament_name}'.")

