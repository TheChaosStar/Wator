from Entity import Poisson, Requin
from Plateau import Plateau
import os, time
clear = lambda: os.system('clear')

SIZE = 2


plateau = Plateau(SIZE)

#plateau.addEntity(Requin(SIZE))
#plateau.addEntity(Requin(SIZE))
#plateau.addEntity(Requin(SIZE))
plateau.addEntity(Requin(SIZE))


# loop
while (True):
    plateau.update()
    print(plateau)

    time.sleep(1)
    
    clear()




