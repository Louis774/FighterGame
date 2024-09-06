#My libraries
from Fighter import Fighter
from Combat import Combat

#Create fighters
player1 = Fighter("Louis", 50, 5, 5, 5)
player2 = Fighter("Gemma", 25, 10, 10, 10)

CombatObject = Combat(0, player1, player2)
CombatObject.startCombat()