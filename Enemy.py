class Enemy:
  type:str
  health:int=10
  attack_damage:int=1

  def __init__(self):
    pass
  
  def Talk(self):
    print(f"I am {self.type},the baddest Enemy, get ready to fight")
  def walk_forward(self):
    print(f"{self.type}, moving closer to attack")
  def attack(self):
    print(f"{self.type} attacks for {self.attack_damage} damage")