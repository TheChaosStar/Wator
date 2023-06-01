from random import randint, randrange


class Entity:
    def __init__(self, x, y, char, breadingCount):
        self.x = x
        self.y = y
        self.char = char
        self.breadingCount = breadingCount
    def __str__(self): return f"X:{self.x} | Y:{self.y} | Char:{self.char}"

    def getX(self): return self.x
    def getY(self): return self.y
    def getChar(self): return self.char
    
    def getAround(self, entities:list)->list:
        """get if other entities in range of this entity

        Args:
            entities (list): list of entities

        Returns:
            list: return list of entities
        """
        entities_in_range = []

        for e in entities:
            if e.x == self.x + 1 or e.x == self.x - 1 or e.y == self.y + 1 or e.y == self.y - 1:
                entities_in_range.append(e)

        return entities_in_range
    def move(self, plateau_size, pos=randint(0, 3)):
        if pos == 0:
            if self.x - 1 < 0: self.x = plateau_size - 1
            else: self.x -= 1 
        elif pos == 1:
            if self.x + 1 > plateau_size - 1: self.x = 0
            else: self.x += 1 
        elif pos == 2:
            if self.y - 1 < 0: self.y = plateau_size - 1
            else: self.y -= 1 
        elif pos == 3:
            if self.y + 1 > plateau_size - 1: self.y = 0
            else: self.y += 1 

# --------------------------------------------------------------------


class Poisson (Entity):
    def __init__(self, size):
        super().__init__(
            randint(0, size - 1),
            randint(0, size - 1),
            "🐟", 0
        )

    def move(self, plateau_size, entities):
        entities_in_range = super().getAround(entities)
        pos_list = [0, 1, 2, 3]


        for e in entities_in_range:
            if e.getX() == self.x - 1: # Up
                pos_list.remove(0)
            elif e.getX() == self.x + 1: # Down
                pos_list.remove(1)
            elif e.getY() == self.y - 1: # Left
                pos_list.remove(2)
            elif e.getY() == self.y + 1: # Right
                pos_list.remove(3)

        if len(pos_list) != 0: 
            rand = randint(0, len(pos_list))
            super().move(plateau_size, rand)


class Requin (Entity):
    def __init__(self, size):
        super().__init__(
            randint(0, size - 1),
            randint(0, size - 1),
            "🦈", 0
        )
        self.power = 5

    def move(self, plateau_size, entities):
        entities_in_range = super().getAround(entities)
        
        for e in entities_in_range:
            if isinstance(e, Poisson): 
                self.x = e.x
                self.y = e.y
                return
            
        super().move(plateau_size)


        
