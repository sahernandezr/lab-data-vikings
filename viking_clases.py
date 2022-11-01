# Soldier


class Soldier:
    #---this is the constructor
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    #--- end of constructor    
    
    def attack(self):
    #function that receives zero arguments and returns the strength property of the Soldier
        return self.strength
    
    def receive_damage(self, damage):
#Function that receives one argument: damage, and removes the damage value from the health property. Doesn't return anything
        self.health -= damage

    
# Viking


class Viking(Soldier):
#Viking is a Soldier with an additional property: their name
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        
    def receive_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            print(f'{self.name} has received {damage} points of damage')
        elif self.health<=0:
            print(f'{self.name} has died in act of combat')
        return self.health
        
    def battle_cry(self):
        return 'Odin Owns You All!'
    

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def receive_damage(self, damage):
        self.health -= damage
        if self.health<=0:
            print(f'A Saxon has died in combat')
        elif self.health > 0:
            print(f'A Saxon has received {damage} points of damage') 
        return self.health
        
# War


class War:

    def __init__(self):
        self.viking_army = []
        self.saxon_army = []
        
    def add_viking(self, Viking):
        self.viking_army.append(Viking)
            
    def add_saxon(self, Saxon):
        self.saxon_army.append(Saxon)
          
    def viking_attack(self):
        x = random.randint(0,len(self.saxon_army)-1)
        saxonrandom = self.saxon_army[x]
        y = random.randint(0,len(self.viking_army)-1)
        vikingrandom = self.viking_army[y]
        saxonrandom.receive_damage(vikingrandom.strength)
        if saxonrandom.health <= 0:
            self.saxon_army.pop(x) 
        return self.saxon_army, saxonrandom.receive_damage(vikingrandom.strength)
                 
    def saxon_attack(self):
        x = random.randint(0,len(self.saxon_army)-1)
        saxonrandom = self.saxon_army[x]
        y = random.randint(0,len(self.viking_army)-1)
        vikingrandom = self.viking_army[y]
        vikingrandom.receive_damage(saxonrandom.strength)
        if vikingrandom.health <= 0:
            self.viking_army.pop(y)
        return self.viking_army, vikingrandom.receive_damage(saxonrandom.strength), vikingrandom.health
         
    def show_status(self):
        if len(self.saxon_army)==0:
            return 'Vikings have won the war of the century'
        if len(self.viking_army)==0:
            return 'Saxons have fought for their lives and survive another day...'
        if len(self.saxon_army)>=1 and len(self.viking_army)>=1:
            return 'Vikings and Saxons are still in the thick of battle.'