class Statline:
    def __init__(
        self,
        model_name: str,
        move: int,
        weapon_skill: int,
        ballistic_skill: int,
        strength: int,
        toughness: int,
        wounds: int,
        attacks: int,
        leadership: int,
        save: int,
    ):
        self.model_name = model_name
        self.move = move
        self.weapon_skill = weapon_skill
        self.ballistic_skill = ballistic_skill
        self.strength = strength
        self.toughness = toughness
        self.wounds = wounds
        self.attacks = attacks
        self.leadership = leadership
        self.save = save

    @classmethod
    def reiver_sergeant(cls):
        return cls("Reiver Sergeant", 6, 3, 3, 4, 4, 2, 3, 8, 3)
