from Enemy import *

class ogre(Enemy):
  def __init__(self,  health,attack_damage):
    super().__init__(type="Ogre",health=health,attack_damage=attack_damage)

  def Talk(self):
    return"slamming hands all around"
  def HuntKids(self):
    return "Hunting kids with appetite"