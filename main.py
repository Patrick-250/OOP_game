from Enemy import *

enemy= Enemy()
enemy.type="Zombie"

enemy.Talk()
enemy.walk_forward()
enemy.attack()
print(f"{enemy.type} has {enemy.health} health points and can do an attack of {enemy.attack_damage}")