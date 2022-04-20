from player import Player
from shipoffoolsgame import ShipOfFoolsGame


class PlayRoom:
    """
        In this room multiple player are added. And Play their game.
        The room will track all the player score and controll the game.
    """
    
    def __init__(self) -> None:
        self._game = None
        self._players = []
        self._winner = None
    
    def set_game(self, game: ShipOfFoolsGame) -> None:
        """set the game

        Args:
            game (ShipOfFoolsGame): Game object, will be played by the players. 
        """
        self._game = game
    
    def add_player(self, player: Player) -> None:
        """Add player to this room

        Args:
            player (Player): player object, who play the game
        """
        self._players.append(player)
    
    def reset_scores(self) -> None:
        """reset scores of the player added in this room.
        """
        for player in self._players:
            player.reset_score()

    def play_round(self) -> None:
        """In a round each player has 3 chances to get a higher score.
        """
        for player in self._players:
            player.play_round(self._game)
    
    def game_finished(self) -> bool:
        """Check if the game is finished or not.

        Returns:
            bool: return True, if the game finished, otherwise return false.
        """
        for player in self._players:
            if player.current_score() >= self._game.get_winning_score():
                self._winner = player
                return True
        return False
    
    def print_scores(self) -> None:
        """Print all player's current score.
        """
        for player in self._players:
            print(f"{player.get_name()}'s score: {player.current_score()}")
    
    def print_winner(self) -> None:
        """print the winner of the game!"""
        print(f"Congratulations {self._winner.get_name()}! You won the match!")