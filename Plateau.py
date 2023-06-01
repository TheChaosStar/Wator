from Entity import *
import os

class Plateau :
    def __init__(self, size) -> None:
        self.running = True
        self.size = size
        self.plateau = [[" • " for i in range(self.size)] for j in range(self.size)]
        self.entities = []

    def isRunning(self) -> bool:
        return self.running

    def addEntity(self, e:Entity):
        self.entities.append(e)
        e.render(self.plateau)

    def removeEntity(self, e:Entity):
        self.entities.remove(e)
        self.update()
    
    def update(self):
        self.plateau.clear()
        self.plateau = [[" • " for i in range(self.size)] for j in range(self.size)]
        
        for e in self.entities:
            e.update(self.size, self.entities)
            e.render(self.plateau)
            
    def render(self):
        string = ""
        for y in range(self.size) :
            for x in range(self.size) :
                string += self.plateau[y][x]
            string += "\n"
        print(string)        