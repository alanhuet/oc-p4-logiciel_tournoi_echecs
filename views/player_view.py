from models.player import Player


class PlayerView:
    def prompt_for_player_data(self):
        """ Displays the player creation form and retrieves the entries. """
        print("\n" + "="*34)
        print("=" + " "*9 + "NOUVEAU JOUEUR" + " "*9 + "=")
        print("="*34 + "\n")
        
        while True:
            last_name = input("Nom de famille : ")
            try:
                Player.validate_last_name(last_name)
                break
            except Exception as e:
                self.show_error_message(e)

        while True:
            first_name = input("Prénom : ")
            try:
                Player.validate_first_name(first_name)
                break
            except Exception as e:
                self.show_error_message(e)

        while True:
            birth_date = input("Date de naissance (JJ/MM/AAAA) : ")
            try:
                Player.validate_birth_date(birth_date)
                break
            except Exception as e:
                self.show_error_message(e)


        while True:
            chess_id = input("Identifiant National d'échecs (ex: AB12345) laissez vide si pas d'identifiant : ")
            try:
                Player.validate_chess_id(chess_id)
                break
            except Exception as e:
                self.show_error_message(e)

        return {
            "last_name": last_name,
            "first_name": first_name,
            "birth_date": birth_date,
            "chess_id": chess_id
        }

    def show_player_created_success(self, first_name, last_name):
        """ Displays a confirmation message. """
        print(f"\n [SUCCÈS] Le joueur {first_name} {last_name} a été créé. ")

    def show_error_message(self, error_message):
        """ Displays a validation error. """
        print(f"\n[ERREUR] {error_message}")

    def display_player_list(self, players):
        print("\n" + "-"*29)
        print("|" + " "*5 + "Liste des joueurs" + " "*5 + "|")
        print("-"*29)
        print("\n" + f"{'NOM':<15} | {'PRÉNOM':<15} | {'ID JOUEUR':<10}")
        print("-"*50)

        for p in players:
            print(f"{p.last_name.upper():<15} | {p.first_name.capitalize():<15} | {p.player_id:<10}")

        print("="*50)
        input("\nAppuyez sur Entrée pour revenir au menu.")