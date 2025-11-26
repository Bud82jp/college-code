class Enemy:
    """ts a class for creating instances of an enemy character for combat encounters"""
    entityType = "Unassigned"
    currentHealth = 100
    maxHealth = 100
    damage = 5
    alive = True
    
    def TakeDamage(self, amount):
        self.currentHealth -= amount
        self.StillAlive()
    def StillAlive(self):
        if self.currentHealth <= 0:
            self.alive = False
