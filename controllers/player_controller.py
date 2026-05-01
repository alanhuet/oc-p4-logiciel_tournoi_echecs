
from models.player import Player
from views.player_view import PlayerView
from models.exceptions import ChessProjectException

class PlayerController:
    def __init__(self):
        self.view = PlayerView()

    def create_player(self):

        data = self.view.prompt_for_player_data()

        try:
            new_player = Player(
                last_name=data["last_name"],
                first_name=data["first_name"],
                birth_date=data["birth_date"],
                chess_id=data["chess_id"]
            )

            self.view.show_player_created_success(
                new_player.first_name,
                new_player.last_name
            )

            return new_player
        
        except ChessProjectException as error:
            self.view.show_error_message(str(error))