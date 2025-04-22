from Enemy import *
from Zombie import *
from ogre import *

def battle(e:Enemy):
 
  e.attack()



Zombie= Zombie(1,10)
ogre=ogre(21,4)

print(Zombie.Talk())
print(ogre.Talk())

print(Zombie.Spread_disease())
print(ogre.HuntKids())

battle(Zombie)
battle(ogre)


