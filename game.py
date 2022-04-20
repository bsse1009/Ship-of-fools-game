import random
from typing import List


class Die:
    """A die has 6 face with 6 values (1-6)
    """
    def __init__(self):
        self._value = None
        
    def roll(self) -> None:
        """Get a random value (1-6)
        """
        rand_int = random.randint(1,6)
        self._value = rand_int
        
    def get_value(self) -> int:
        """rturn the value after rolling the die

        Returns:
            int: the value of die's face after rolling
        """
        return self._value


class DiceCup:
    """
        A dice cup contain 5 dice
        Once it roll, five value will be faced from five dices.
    """
    def __init__(self) -> None:
        self._dice = []
        self._banked_dice = []
        self._values = []
        self.put_die_in_dice()
        
    def put_die_in_dice(self) -> None:
        """add 5 die in dice list
        """
        for i in range(5):
            die = Die()
            self._dice.append(die)
            
    def value(self, index: int) -> int:
        """Get a particular die value by index

        Args:
            index (int): Index of die in dice (0-4)

        Returns:
            int : the value of the die which index was passed
        """
        return self._dice[index].get_value()
    
    def bank(self, index: int) -> None:
        """Bank a die in dice list by its index

        Args:
            index (int): Index of die in dice (0-4)
        """
        self._banked_dice.append(self._dice[index])
        
    def is_banked(self, index: int) -> bool:
        """check if a die is banked or not

        Args:
            index (int): Index of die in dice (0-4)

        Returns:
            bool: If the die is banked then return true, else return false
        """
        if self._dice[index] not in self._banked_dice:
            return False
        return True
    
    def release(self, index: int) -> None:
        """realease the banked die by its index

        Args:
            index (int): Index of die in dice (0-4)
        """
        self._banked_dice.remove(self._dice[index])
        
    def release_all(self) -> None:
        """realese all the banked dice
        """
        self._banked_dice = []
        
    def roll(self) -> None:
        """Roll the dice
        """
        self._values = []
        for die in self._dice:
            if die not in self._banked_dice:
                die.roll()
                self._values.append(die.get_value())
                
    def get_rolled_result(self) -> List:
        """return all the values after rolled dice

        Returns:
            List: List of dice values
        """
        return self._values
    
    
class ShipOfFoolsGame:
    """This class is responsible for Core Game Logic."""    

    def __init__(self, winning_score: int) -> None:
        """Initializing the class attributes

        Args:
            winning_score (int): [It is a boundary value of the game, If a player reach the winning score, the game will over]
        """

        self._cup = DiceCup()
        self._winning_score = winning_score
        self._num_of_roll_allowed = 3
        self._status = [False, False, False]
        self._score = 0
        
    def round(self, player_name: str) -> None:
        """In Every round each player has 3 chances to make a better score. In every chances player roll the unbanked dices and get a score.

        Args:
            player_name (str): [It help to recognize which player play the round!]
        """
        
        self.__init__(21)   # Initialize all values for new round!
        
        print(f"{player_name} turn: ")
        
        while self._num_of_roll_allowed>0:
            self._cup.roll()
            values = self._cup.get_rolled_result()
            self.print_values(values)
            self.evalute(values)
            self._num_of_roll_allowed = self._num_of_roll_allowed-1
            
    def evalute(self, values: List) -> None:
        """The fuction evalute the rolled dice. It check if the dices has ship, captain and crew or not. 

        Args:
            values (List): [Resultant values or rolled dices]

        Returns:
            [type]: [None]
        """
        
        if self._status[0] == False:    # If We don't have the ship
            if 6 in values:
                self._status[0] = True
                self._cup.bank(0)
                values.remove(6)
            else:
                return # break the method because we dont even have the ship
            
        if self._status[1] == False:    # We have ship but we don't have the captain
            if 5 in values:
                self._status[1] = True
                self._cup.bank(1)
                values.remove(5)
            else:
                return # break the method because we dont have the captain
            
        if self._status[2] == False:    # We have ship and captain but we don't have the crew
            if 4 in values:
                self._status[2] = True
                self._cup.bank(2)
                values.remove(4)
            else:
                return # break the method because we dont have the crew
            
        # We are here, that means the ship, captain and crew are availabe. Now we looking for the scores
        self._score = sum(values)
            
    def get_score(self) -> int:
        """Get the current round score

        Returns:
            int: current round score
        """
        return self._score
    
    def get_winning_score(self) -> int:
        """get wiining score

        Returns:
            int: winning score
        """
        return self._winning_score
    
    def print_values(self, values: List) -> None:
        """print the values after rolling the dices

        Args:
            values (List): vallues of rolled dices
        """
        all_values = []
        value = 6
        # The dices who are not rolled, If find 6 in previous chances, we keep this dice.
        for i in range (3):
            if self._status[i] == True:
                all_values.append(value)
                value -= 1
            else: break
        # the dices who are rolled 
        for val in values:
            all_values.append(val)
        print(all_values) 


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
        


if __name__ =="__main__":
    """
        The main loop of the game
        create a playroom
        create a game instances
        create player instances 
        add game and players in playroom
        loop the game until the game finished
    """
    room = PlayRoom()
    game = ShipOfFoolsGame(21)
    room.set_game(game)
    player1 = Player()
    player1.set_name("Player 1")
    player2 = Player()
    player2.set_name("Player 2")
    room.add_player(player1)
    room.add_player(player2)
    room.reset_scores()
    while not room.game_finished():
        room.play_round()
        room.print_scores()
    room.print_winner()