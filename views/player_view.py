


class PlayerView:
    def prompt_for_player_data(self):
        """ Displays the player creation form and retrieves the entries. """
        print("\n" + "="*34)
        print("=" + " "*9 + "NOUVEAU JOUEUR" + " "*9 + "=")
        print("="*34 + "\n")

        last_name = input("Nom de famille : ")
        first_name = input("Prénom : ")
        birth_date = input("Date de naissance (JJ/MM/AAAA) : ")
        chess_id = input("Identifiant National d'échecs (ex: AB12345) : ")

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