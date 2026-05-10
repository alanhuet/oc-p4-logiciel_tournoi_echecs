
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController

def test_tournament():
    controller = TournamentController()
    controller.create_tournament()

#def main():
#    controller = PlayerController()
#    controller.create_player()

if __name__ == "__main__":
    test_tournament()