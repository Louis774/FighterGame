from Utility import Utility
import time

class Combat:
    fightOrder = []
    #Combat class, once created can start combat
    def __init__(self, roundNumber, ally, enemy):
        self.RoundNumber = roundNumber
        self.Ally = ally
        self.Enemy = enemy

    def createOrder(self):
        if self.Ally.Agility > self.Enemy.Agility:
            self.fightOrder.append(self.Ally)
            self.fightOrder.append(self.Enemy)

        #If agility is tied, randomise
        elif self.Ally.Agility == self.Enemy.Agility:
            n = Utility.rollDice(2)
            if n == 1:
                self.fightOrder.append(self.Ally)
                self.fightOrder.append(self.Enemy)
            else:
                self.fightOrder.append(self.Enemy)
                self.fightOrder.append(self.Ally)
            
        else:
            self.fightOrder.append(self.Enemy)
            self.fightOrder.append(self.Ally)


    def startCombat(self):
        print("Combat starts")
        self.nextRound()

    def nextRound(self):
        self.RoundNumber += 1
        print("Round ", self.RoundNumber)
        
        time.sleep(0.5)
        
        self.createOrder()

        self.fightOrder[0].attack(self.fightOrder[1])