import random


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