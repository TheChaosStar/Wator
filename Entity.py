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
    def move(self):
        randPos = randint(0, 3)
        if randPos == 0:
            if self.x - 1 < 0: self.x = plateau_size - 1
            else: self.x -= 1 
        if randPos == 1:
            if self.x + 1 > plateau_size - 1: self.x = 0
            else: self.x += 1 
        if randPos == 2:
            if self.y - 1 < 0: self.y = plateau_size - 1
            else: self.y -= 1 
        if randPos == 3:
            if self.y + 1 > plateau_size - 1: self.y = 0
            else: self.y += 1 

# --------------------------------------------------------------------


class Poisson (Entity):
    def __init__(self, size):
        super().__init__(
            randint(0, size),
            randint(0, size),
            "🐟", 0
        )

    # def move(self, entities):
    #     list_of_dir = super().getAround(entities)
    #     move_dir = []

    #     if len(list_of_dir) != 0:
    #         if list_of_dir.index("R"): list_of_dir.remove("R")
    #         if list_of_dir.index("L"): list_of_dir.remove("L")
    #         if list_of_dir.index("U"): list_of_dir.remove("U")
    #         if list_of_dir.index("D"): list_of_dir.remove("D")
    #         move_dir = list_of_dir[randrange(0, len(list_of_dir))]
    #     else: move_dir = ["R", "L", "U", "D"]

    #     if move_dir == "R": self.x += 1
    #     if move_dir == "L": self.x -= 1
    #     if move_dir == "U": self.y += 1
    #     if move_dir == "D": self.y -= 1



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
            
        super().move()


        
