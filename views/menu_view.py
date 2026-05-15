
class AppView:
    def display_main_menu(self):
        """ Displays the main menu and retrieves the user's choice. """
        print("\n" + "="*35)
        print("=" + " "*10 + "CENTRE ÉCHECS" + " "*10 + "=")
        print("="*35 + "\n")
        print("1. Gestion des joueurs")
        print("2. Gestion des tournois")
        print("3. Rapports")
        print("4. Quitter")

        return input("\nVotre choix : ")
    
    def display_player_menu(self):
        """ Displays the player management submenu. """
        print("\n" + "="*41)
        print("=" + " "*10 + "GESTION DES JOUEURS" + " "*10 + "=")
        print("="*41 + "\n")
        print("1. Créer un nouveau joueur")
        print("2. Retour au menu principal")

        return input("\nVotre choix :")
    
    def display_tournament_menu(self):
        """ Displays the tournament management submenu. """
        print("\n" + "="*42)
        print("=" + " "*10 + "GESTION DES TOURNOIS" + " "*10 + "=")
        print("="*42 + "\n")
        print("1. Créer un nouveau tournoi")
        print("2. Gérer les participants (Ajouter/Retirer)")
        print("3. Lancer / Reprendre un tournoi")
        print("4. Retour au menu principal")

        return input("\nVotre choix :")
    
    def display_reports_menu(self):
        """ Displays the reports submenu. """
        print("\n" + "="*30)
        print("=" + " "*10 + "RAPPORTS" + " "*10 + "=")
        print("="*30 + "\n")
        print("1. Liste de tous les joueurs")
        print("2. Liste de tous les tournois")
        print("3. Rapports détaillés d'un tournoi")
        print("4. Retour au menu principal")

        return input("\nVotre choix :")
    
    def display_tournament_details_menu(self, tournament_name):
        """ Submenu appears once a tournament is selected. """
        print(f"\n--- RAPPORT : {tournament_name} ---")
        print("\n1.Nom et Dates")
        print("2. Liste des joueurs inscrits")
        print("3. Liste des Rounds et Matchs")
        print("4. Vue d'ensemble (tout afficher)")
        print("5. Revenir à la sélection du tournoi")

        return input("\nVotre choix :")