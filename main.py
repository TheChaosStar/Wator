from Entity import Poisson, Requin
from Plateau import Plateau
import os, time
clear = lambda: os.system('clear')

SIZE = 2


plateau = Plateau(SIZE)

plateau.addEntity(Poisson(SIZE))
plateau.addEntity(Requin(SIZE))

frame = 1

# loop
while (plateau.isRunning()):
    print(f"[{frame}]")

    plateau.update()
    plateau.render()

    time.sleep(.25)
    
    clear()
    frame += 1




