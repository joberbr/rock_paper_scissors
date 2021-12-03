"""A module to create the classes for a Rock, Paper, Scissors game."""


class Roll:
    """Creates a roll object with the name and what it defeats and what it loses to."""

    def __init__(self, name, defeat, lose):
        self.name = name
        self.defeat = defeat
        self.lose = lose

    def can_defeat(self, roll):
        """Determines if it can defeat the current roll."""
        return roll.name == self.defeat

    def defeated_by(self, roll):
        """Determines if it is defeated by the current roll"""
        return roll.name == self.lose


class Player:
    """Creates a player object with a name."""

    def __init__(self, name):
        self.name = name
