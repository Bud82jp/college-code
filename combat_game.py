from random import Random

class Player:
    """ts a class for creating instances of a player character for combat encounters"""
    entityType = "Unassigned"
    currentHealth = 100
    maxHealth = 100
    damage = 10
    alive = True

    def TakeDamage(self, amount):
        self.currentHealth -= amount
        self.StillAlive()

    def StillAlive(self):
        if self.currentHealth <= 0:
            self.alive = False


class Enemy:
    """ts a class for creating instances of an enemy character for combat encounters"""
    entityType = "Unassigned"
    currentHealth = 100
    maxHealth = 100
    damage = 5
    alive = True
    rand = Random()
    
    def TakeDamage(self, amount):
        self.currentHealth -= amount
        self.StillAlive()

    def StillAlive(self):
        if self.currentHealth <= 0:
            self.alive = False

    def Attack(self, target):
        target.TakeDamage(self.damage)

    def DecideAction(self, target):
        decision = Enemy.rand.randint(1, 3)
        match decision:
            case 1:
                self.Attack(target)
            case 2:
                pass
                # self.Dodge(2)
            case 3:
                pass
                # self.Parry(3)


p = Player()
enemies = []
enemies.append(Enemy())
enemies.append(Enemy())

for x in ememies:
    x.DecideAction(p)