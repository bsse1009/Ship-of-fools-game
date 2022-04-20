from typing import List
from die import Die


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