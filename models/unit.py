from models.ability import Ability
from models.specialism import Specialism
from models.statline import Statline
from models.weapon import Weapon


class Unit:
    def __init__(
        self,
        name: str,
        unit_name: str,
        statline: Statline,
        weapons: Weapon,
        abilities: Ability,
        specialism: Specialism = None,
        demeanour=None,
    ):
        self.name = name
        self.unit_name = unit_name
        self.statline = statline
        self.weapons = weapons
        self.abilities = abilities
        self.specialism = specialism
        self.demeanour = demeanour

    @classmethod
    def ulfrich_wyrmslayer(cls):
        return cls(
            "Ulfrich Wyrmslayer",
            "Reiver Sergeant",
            Statline.reiver_sergeant,
            [
                Weapon.bolt_carbine,
                Weapon.heavy_bolt_pistol,
                Weapon.frag_grenade,
                Weapon.krak_grenade,
                Weapon.shock_grenade,
            ],
            "abilities_ph",
            Specialism.leader,
            "Noble",
        )

    # @property
    # def specialism(self):
    #     return self.specialism
