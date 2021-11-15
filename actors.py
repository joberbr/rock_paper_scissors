class Roll:
    def __init__(self, name, defeat):
        self.name = name
        self.defeat = defeat

    def can_defeat(self, roll):
        return roll.name == self.defeat


class Player:
    def __init__(self, name):
        self.name = name
