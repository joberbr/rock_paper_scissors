class Roll:
    def __init__(self, name, defeat, lose):
        self.name = name
        self.defeat = defeat
        self.lose = lose

    def can_defeat(self, roll):
        return roll.name == self.defeat

    def defeated_by(self, roll):
        return roll.name == self.lose


class Player:
    def __init__(self, name):
        self.name = name
