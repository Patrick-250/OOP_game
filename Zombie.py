from Enemy import *
#zombie is a child class of enemy and it should inherit all its methods and props
class Zombie(Enemy):
   def __init__(self,  health,attack_damage):
      super().__init__(type="Zombie",health=health,attack_damage=attack_damage)

    #override the talk method from Enemy class
   def Talk(self):
      print("***crumbling***")
   #create a spread disease that is unique to zombie class
   def Spread_disease(self):
      print("spreading infections")