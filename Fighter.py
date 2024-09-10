class Fighter:
    #Fighter class
    def __init__(self, name, health, strength, agility, intellect):
        self.Name = name
        self.Health = health
        self.Strength = strength
        self.Agility = agility
        self.Intellect = intellect

    def attack(self, attacking):
        dmg = 3 + self.Strength
        print("{0} attacks {1} and deals {2} damage!".format(self.Name, attacking.Name, dmg))

        attacking.Health -= dmg
