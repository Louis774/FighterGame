#My libraries
from Fighter import Fighter
from Combat import Combat

#Create fighters
player1 = Fighter("Louis", 50, 20, 5, 5)
player2 = Fighter("Gemma", 25, 10, 10, 10)
player3 = Fighter("James", 50, 5, 7, 10)
player4 = Fighter("Molly", 30, 6, 9, 6)


CombatObject = Combat(0, [player1, player2], [player3, player4])
CombatObject.startCombat()