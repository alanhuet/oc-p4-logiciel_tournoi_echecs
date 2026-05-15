
from models.player import Player
from views.player_view import PlayerView
from models.exceptions import ChessProjectException
from models.storage import StorageManager

class PlayerController:
    def __init__(self):
        self.view = PlayerView()
        self.storage = StorageManager("players")
        self.players = [Player.from_dict(p) for p in self.storage.load()]

    def create_player(self):

        data = self.view.prompt_for_player_data()

        try:
            new_player = Player(
                last_name=data["last_name"],
                first_name=data["first_name"],
                birth_date=data["birth_date"],
                chess_id=data["chess_id"]
            )

            self.players.append(new_player)
            self.save_all_players()

            self.view.show_player_created_success(
                new_player.first_name,
                new_player.last_name
            )

            return new_player
        
        except ChessProjectException as error:
            self.view.show_error_message(str(error))

        

    def save_all_players(self):
        data_to_save = [player.to_dict() for player in self.players]
        self.storage.save(data_to_save)

    def list_players_alphabetically(self):
        sorted_players = sorted(
            self.players,
            key=lambda p: p.last_name.lower()
        )
        if not sorted_players:
            self.view.show_error_message("Aucun joueur enregistré.")
        else:
            self.view.display_player_list(sorted_players)
