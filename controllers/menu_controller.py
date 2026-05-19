
from views.menu_view import AppView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController

class AppController:
    def __init__(self):
        self.view = AppView()
        self.player_control = PlayerController()
        self.tournament_control = TournamentController()

    def run(self):

        while True:
            choice = self.view.display_main_menu()

            if choice == "1":
                self.run_player_menu()
            elif choice == "2":
                self.run_tournament_menu()
            elif choice == "3":
                self.run_reports_menu()
            elif choice == "4":
                print("\nFermeture du programme.")
                break
            else:
                print("\n[ERREUR] choix invalide. Veuillez saisir un chiffre entre 1 et 4.")        

    def run_player_menu(self):

        while True:
            choice = self.view.display_player_menu()
            if choice == "1":
                self.player_control.create_player()
            elif choice == "2":
                break

    def run_tournament_menu(self):

        while True:
            choice = self.view.display_tournament_menu()
            if choice == "1":
                self.tournament_control.create_tournament()
            elif choice == "2":
                self.tournament_control.manage_tournament_participants()
            elif choice == "3":
                self.tournament_control.play_tournament()
            elif choice == "4":
                break

    def run_reports_menu(self):

        while True:
            choice = self.view.display_reports_menu()
            if choice == "1":
                self.player_control.list_players_alphabetically()
            elif choice == "2":
                #affiche la liste des tournois
                ...
            elif choice == "3":
                self.run_tournament_detail_menu()
            elif choice == "4":
                break

    def run_tournament_detail_menu(self):

        while True:
            choice = self.view.display_tournament_details_menu("mettre variable pour nom du tournoi")
            if choice == "1":
                #affiche le nom et la date du tournoi
                ...
            elif choice == "2":
                #affiche l liste des joureurs inscrits au tournoi
                ...
            elif choice == "3":
                #affiche la liste des rounds et des matchs
                ...
            elif choice == "4":
                #affiche l'ensemble des éléments 1,2 et 3
                ...
            elif choice == "5":
                break

  