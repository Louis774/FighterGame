from Utility import Utility
import time
import copy

'''
combat order:

1. Highest agility starts
2. Attack enemy
3. Damage is based on strength
4. If higher intellect, chance for critical hit

'''




class Combat:
    fightOrder = []
    #Combat class, once created can start combat
    def __init__(self, roundNumber, leftSide, rightSide):
        self.roundNumber = roundNumber
        self.leftSide = leftSide
        self.rightSide = rightSide

    def createOrder(self):
        #Quicksort algorithm
        def partition(arr, low, high):
            pivot = arr[high].Agility

            i = low - 1

            for j in range(low, high):
                if arr[j].Agility > pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1
        
        def quicksort(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)

                quicksort(arr, low, pi - 1)
                quicksort(arr, pi + 1, high)

        # Create an array of all the fighters
        allFighters = []
        for fighter in self.leftSide:
            allFighters.append(fighter)
        for fighter in self.rightSide:
            allFighters.append(fighter)
        
        # Sort by agility
        quicksort(allFighters, 0, len(allFighters) - 1)

        self.fightOrder = allFighters


    def announceSide(self, side):
        #Print all players on a certain side
        string = ""
        for i in side:
            string = string + i.Name + " and "
        
        newString = string.rsplit(' ', 2)[0]

        return newString
    

    def startCombat(self):
        print("Combat starts.")
        #Print the roster
        print("{0} vs {1}".format(self.announceSide(self.leftSide), self.announceSide(self.rightSide)))

        time.sleep(1)

        self.nextRound()

    def nextRound(self):
        self.roundNumber += 1
        print("Round ", self.roundNumber)
        
        time.sleep(0.5)
        
        # Create the fight order
        self.createOrder()

        #Loop through and process attacks
        for fighter in self.fightOrder:
            #Check which side they are on
            if fighter in self.leftSide:
                target = self.rightSide[Utility.rollDice(len(self.rightSide))-1]
                fighter.attack(target)

                if target.Health <= 0:
                    print(target.Name, " has fallen!")
                    self.rightSide.remove(target)
            elif fighter in self.rightSide:
                target = self.leftSide[Utility.rollDice(len(self.leftSide))-1]
                fighter.attack(target)

                if target.Health <= 0:
                    print(target.Name, " has fallen!")
                    self.leftSide.remove(target)
            
            if len(self.leftSide) == 0 or len(self.rightSide) == 0:
                break

            time.sleep(1)

        if len(self.leftSide) == 0:
            print(self.announceSide(self.rightSide), " is victorious!")
        elif len(self.rightSide) == 0:
            print(self.announceSide(self.leftSide), " is victorious!")
        else:
            self.nextRound()