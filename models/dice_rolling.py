import random


class DiceRolls:

    def __init__(self):
        pass

    def dice_rolls(self, number_of_dice: int, number_of_sides: int=6) -> list:
        """
        Rolls a dice with number_of_sides sides number_of_dice times and returns a
        sorted list
        """
        dice_rolls = []
        for roll in range(number_of_dice):
            dice_rolls.append(random.randint(1, number_of_sides))
        dice_rolls.sort()

        return dice_rolls

    def attack_roll(self, target:models.Unit, number_of_dice: int, number_of_sides: int=6) -> list:  #TODO: move to unit or subclass of unit?
        """

        """
        pass
