class Specialism:
    def __init__(self, name: str, level: int, tactics: list):
        self.name = name
        self.level = level
        self.tactics = tactics

    @classmethod
    def leader(cls):
        return cls("Leader", 1, ["Resourceful"])
