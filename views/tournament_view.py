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

    def display_tournament_play_menu(self, tournament_name, round_num, in_progress):
        """ Displays the contextual action menu according to the round status. """
        status = "EN COURS" if in_progress else "À LANCER"
        print("\n" + "="*50)
        print(f"TOURNOI : {tournament_name.upper()} | ROUND {round_num} ({status})")
        print("="*50)

        if not in_progress:
            print("1. Générer et démarrer le Round")
        else:
            print("1. Saisir les résultats et clôturer le Round")
        print("2. Retour")

        return input("\nVotre choix : ")
    
    def display_round_pairings(self, round_name, matches):
        """ Displays the generated encounters. """
        print(f"\n--- MATCHS DU {round_name.upper()} ---")
        for i, ((p1, _), (p2, _)) in enumerate(matches, 1):
            print(f"Match {i} : {p1.last_name.upper()} {p1.first_name} VS {p2.last_name.upper()} {p2.first_name}")
        print("_"*40)
        input("\nPrenez note des matchs et appuyez sur Entrée pour continuer...")

    def prompt_for_match_score(self, match_num, p1,p2):
        """ Request the result of a match in a guided manner. """
        print(f"\n[Match {match_num}] {p1.last_name.upper()} VS {p2.last_name.upper()}")
        print("1 : Victoire de " + p1.last_name.upper())
        print("2 : Victoire de " + p2.last_name.upper())
        print("3 : Match nul")

        while True:
            choice = input("Résultat du match (choisir 1, 2 ou 3) :")
            if choice == "1":
                return 1.0, 0.0
            elif choice == "2":
                return 0.0, 1.0
            elif choice == "3":
                return 0.5, 0.5
            print("[ERREUR] Saisie invalide. Entrez 1, 2 ou 3.")

    def display_round_summary(self, matches):
        """ Displays a summary of the round scores before validation. """
        print("\n--- RÉCAPITULATIF DES RÉSULTATS ---")
        for i, ((p1, s1), (p2, s2)) in enumerate(matches, 1):
            print(f"Match {i} : {p1.last_name.upper()} ({s1}) VS {p2.last_name.upper()} ({s2})")
        print("-"*35)

        return input("Valider ces scores et clôturer le round ? (y/n) :").lower() == "y"




