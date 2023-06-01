from Entity import Poisson, Requin
from Plateau import Plateau
import os, time
clear = lambda: os.system('clear')

SIZE = 5


plateau = Plateau(SIZE)

#plateau.addEntity(Requin(SIZE))
#plateau.addEntity(Requin(SIZE))
#plateau.addEntity(Requin(SIZE))
plateau.addEntity(Poisson(SIZE))
plateau.addEntity(Requin(SIZE))

plateau.update()
print(plateau)

plateau.update()
print(plateau)

plateau.update()
print(plateau)

# loop
# while (True):

#     plateau.update()
#     print(plateau)

#     time.sleep(1)
    
#     clear()




