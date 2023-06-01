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

    def getAround(self, entities: list) -> list:
        """get if other entities in range of this entity

        Args:
            entities (list): list of entities

        Returns:
            list: return list of entities
        """
        entities_in_range = []

        for e in entities:
            if e != self:
                if e.x == self.x + 1 or\
                   e.x == self.x - 1 or\
                   e.y == self.y + 1 or\
                   e.y == self.y - 1:
                    entities_in_range.append(e)

        return entities_in_range

    def move(self, plateau_size, pos=randint(0, 3)):
        if pos == 0:
            if self.x - 1 < 0:
                self.x = plateau_size - 1
            else:
                self.x -= 1
        elif pos == 1:
            if self.x + 1 > plateau_size - 1:
                self.x = 0
            else:
                self.x += 1
        elif pos == 2:
            if self.y - 1 < 0:
                self.y = plateau_size - 1
            else:
                self.y -= 1
        elif pos == 3:
            if self.y + 1 > plateau_size - 1:
                self.y = 0
            else:
                self.y += 1

    def update(self, plateau_size, entities=None):
        self.move(plateau_size)

    def render(self, plateau):
        plateau[self.y][self.x] = self.char + " "

# --------------------------------------------------------------------


class Poisson (Entity):
    def __init__(self, size):
        super().__init__(
            randint(0, size - 1),
            randint(0, size - 1),
            "🐟", 0
        )

    def update(self, plateau_size, entities: list):
        entities_in_range = super().getAround(entities)
        pos_list = [0, 1, 2, 3]

        for e in entities_in_range:
            if isinstance(e, Poisson):
                if self.x == 0 and e.getX() == plateau_size - 1 and self.y == e.getY():
                    pos_list.remove(0)
                    break
                if self.x == plateau_size - 1 and e.getX() == 0 and self.y == e.getY():
                    pos_list.remove(1)
                    break
                if self.y == 0 and e.getY() == plateau_size - 1 and self.x == e.getX():
                    pos_list.remove(2)
                    break
                if self.y == plateau_size - 1 and e.getY() == 0 and self.x == e.getX():
                    pos_list.remove(3)
                    break
                if e.getX() == self.x - 1:  # Up
                    pos_list.remove(0)
                if e.getX() == self.x + 1:  # Down
                    pos_list.remove(1)
                if e.getY() == self.y - 1:  # Left
                    pos_list.remove(2)
                if e.getY() == self.y + 1:  # Right
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

    def update(self, plateau_size, entities: list):
        entities_in_range = super().getAround(entities)
        pos_list = []

        for e in entities_in_range:
            if isinstance(e, Poisson):
                if self.x == 0 and e.getX() == plateau_size - 1 and self.y == e.getY():
                    pos_list.append(0)
                    break
                if self.x == plateau_size - 1 and e.getX() == 0 and self.y == e.getY():
                    pos_list.append(1)
                    break
                if self.y == 0 and e.getY() == plateau_size - 1 and self.x == e.getX():
                    pos_list.append(2)
                    break
                if self.y == plateau_size - 1 and e.getY() == 0 and self.x == e.getX():
                    pos_list.append(3)
                    break
                if e.getX() == self.x - 1:  # Up
                    pos_list.append(0)
                if e.getX() == self.x + 1:  # Down
                    pos_list.append(1)
                if e.getY() == self.y - 1:  # Left
                    pos_list.append(2)
                if e.getY() == self.y + 1:  # Right
                    pos_list.append(3)

        if len(pos_list) == 0:
            super().move(plateau_size, randint(0, 3))
        else:
            rand = randint(0, len(pos_list))
            super().move(plateau_size, rand)

        for e in entities_in_range:
            if self.x == e.getX() and self.y == e.getY() and isinstance(e, Poisson):
                self.eat(e)

    def eat(self, entity:Poisson):
        del(entity)
