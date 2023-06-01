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
                string += self.plateau[y][x]
            string += "\n"
        return string

    def addEntity(self, e:Entity) -> None:
        self.entities.append(e)
        #self.update()

    def removeEntity(self, e:Entity) -> None:
        self.entities.remove(e)
        self.plateau[e.getY()][e.getX()] = " • "
    
    def update(self) -> None:
        self.plateau.clear()
        self.plateau = [[" • " for i in range(self.size)] for j in range(self.size)]


        for e in self.entities:
            print(e)


            self.plateau[e.getY()][e.getX()] = e.getChar() + " "
            e.move(self.size, self.entities)

            # for e2 in self.entities:
            #     if e == e2: continue
            #     if e.getX() == e2.getX() and e.getY() == e2.getY():
            #        if isinstance(e, Poisson): self.removeEntity(e)
            #        elif isinstance(e2, Poisson): self.removeEntity(e2)
