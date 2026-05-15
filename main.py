
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.menu_controller import AppController

#def test_tournament():
#    controller = TournamentController()
#    controller.create_tournament()

def main():
   controller = AppController()
   controller.run()

if __name__ == "__main__":
    main()