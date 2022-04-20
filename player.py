from shipoffoolsgame import ShipOfFoolsGame


class Player:
    """
        Player class provides  all the attributes and methods of a player.
        Player can play game.
        A player has a name and score attribute
        A player has a play role (method)
    """
    
    def __init__(self) -> None:
        self._name = None
        self._score = 0     # Obtained total score for a player
        
    def set_name(self, name: str) -> None:
        self._name = name
        
    def get_name(self) -> str:
        return self._name
        
    def current_score(self) -> int:
        return self._score
    
    def reset_score(self) -> None:
        self._score = 0
    
    def play_round(self, game: ShipOfFoolsGame)  -> None:
        """Player play rounds to gain winning scores

        Args:
            game (ShipOfFoolsGame): The Playing Game object
        """
        
        game.round(self._name)
        print(f"In this round you scored: {game.get_score()}")
        self._score += game.get_score()
        return