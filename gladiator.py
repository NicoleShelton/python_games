import random


class Gladiator:
    """ Has strong attributes and methods. """

    def __init__(self, name, health, rage, damage_low, damage_high):
        """ (Gladiator, str, str, str, str, str) -> NoneType
        Create a new gladiator with health, rage, damage_low, damage_high.
        """
        self.name = name
        self.health = health
        self.rage = rage
        self.dam_low = damage_low
        self.dam_high = damage_high

    def attack(self, other):
        """ (Gladiator, Gladiator) -> int
        Return the attack and remaining health and rage.
        """
        hits = random.randint(self.dam_low, self.dam_high)
        if self.rage > random.randint(0, 100):
            hits *= 2
            self.rage = 0
            other.health = other.health - hits
            return '{0} was crit for {1} damage!'.format(other.name, hits)
        else:
            self.rage += 15
            other.health -= hits
            return '{0} was hit for {1} damage!'.format(other.name, hits)

    def heal(self):
        """ (Gladiator) -> int
        Return the health and decreases the rage.
        """
        if self.rage >= 10:
            self.health += 5
            self.rage -= 10
        print('Gladiator healed!')

    def is_dead(self, other):
        """ (Gladiator) -> str
        Return dead iff the Gladiator is dead.
        """
        if self.health < 1:
            dead = 'You are dead...'
        elif other.health < 1:
            dead = 'Opponent is dead...'
        else:
            dead = 'Both gladiators are alive...'
        return dead

    def __str__(self):
        return '{0}, {1}, {2}, {3}'.format(self.health, self.rage,
                                           self.dam_low, self.dam_high)

    def __repr__(self):
        return 'Gladiator({0}, {1}, {2}, {3})'.format(
            self.health, self.rage, self.dam_low, self.dam_high)
