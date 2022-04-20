from typing import List
from dicecup import DiceCup


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