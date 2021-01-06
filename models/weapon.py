from typing import Union


class Weapon:
    def __init__(
        self,
        name: str,
        weapon_range: int,
        weapon_type: str,
        strength: int,
        armour_penetration: int,
        damage: Union[int, str],
        abilities: str = None,
    ):
        self.name = name
        self.weapon_range = weapon_range
        self.weapon_type = weapon_type
        self.strength = strength
        self.armour_penetration = armour_penetration
        self.damage = damage
        self.abilities = abilities

    @classmethod
    def bolt_carbine(cls):
        return cls("Bolt Carbine", 24, "Assault 2", 4, 0, 1)

    @classmethod
    def heavy_bolt_pistol(cls):
        return cls("Heavy Bolt Pistol", 12, "Pistol 1", 4, -1, 1)

    @classmethod
    def frag_grenade(cls):
        return cls("Frag Grenade", 6, "Grenade D6", 3, 0, 1)

    @classmethod
    def krak_grenade(cls):
        return cls("Krak Grenade", 6, "Grenade 1", 6, -1, "D3")

    @classmethod
    def shock_grenade(cls):
        return cls("Shock Grenade", 6, "Grenade D3", "*", "*", "*", "See Core Manual")
