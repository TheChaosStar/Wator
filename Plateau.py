from Entity import *

class Plateau :
    def __init__(self, size) -> None:
        self.size = size
        self.plateau = [[" • " for i in range(self.size)] for j in range(self.size)]
        self.entities = []

    def __str__(self) -> str:
        string = ""
        for y in range(self.size) :
            for x in range(self.size) :
                string += self.plateau[x][y]
            string += "\n"
        return string

    def addEntity(self, e:Entity) -> None:
        self.entities.append(e)
        self.update()

    def removeEntity(self, e:Entity) -> None:
        self.entities.remove(e)
        self.plateau[e.getX()][e.getY()] = " • "
    
    def update(self) -> None:
        self.plateau.clear()
        self.plateau = [[" • " for i in range(self.size)] for j in range(self.size)]

        for e in self.entities:
            for e2 in self.entities:
                if e.getX() == e2.getX() and e.getY() == e2.getY():
                    if isinstance(e, Poisson): self.removeEntity(e)
                    if isinstance(e2, Poisson): self.removeEntity(e)

            print(e)

            self.plateau[e.getX()][e.getY()] = e.getChar() + " "
            e.move(self.size, self.entities)