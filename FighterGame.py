import time
import random

class Utility:
    #Non-object class with a bunch of useful functions

    def rollDice(num):
        return random.randint(1, num)
    

class Fighter:
    #Fighter class
    def __init__(self, name, strength, agility, intellect):
        self.Name = name
        self.Strength = strength
        self.Agility = agility
        self.Intellect = intellect

player1 = Fighter("Louis", 5, 5, 5)
player2 = Fighter("Gemma", 10, 10, 10)

class Combat:
    fightOrder = []
    #Combat class, once created can start combat
    def __init__(self, roundNumber, ally, enemy):
        self.RoundNumber = roundNumber
        self.Ally = ally
        self.Enemy = enemy

    def whoStarts():
        if self.Ally.Agility > self.Enemy.Agility:
            fightOrder.append(self.Ally)
            fightOrder.append(self.Enemy)

        #If agility is tied, randomise
        elif self.Ally.Agility == self.Enemy.Agility:
            n = Utility.rollDice(2)
            if n == 1:
                fightOrder.append(self.Ally)
                fightOrder.append(self.Enemy)
            else:
                fightOrder.append(self.Enemy)
                fightOrder.append(self.Ally)
            
        else:
            fightOrder.append(self.Enemy)
                fightOrder.append(self.Ally)
            


    def startCombat():
        NextRound()

    def nextRound():
        self.RoundNumber += 1
        firstAttack = whoStarts()

        
