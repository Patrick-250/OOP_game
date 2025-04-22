class Enemy:
  def __init__(self,  type:str,health:int=10,attack_damage:int=1):
     self.__type=type
     self.health=health
     self.attack_damage=attack_damage
  def getType(self):
    return self.__type
  

  def Talk(self):
    print(f"I am {self.__type}, get ready to fight")
  def walk_forward(self):
    print(f"{self.__type}, moving closer to attack")
  def attack(self):
    print(f"{self.__type} attacks for {self.attack_damage} damage")