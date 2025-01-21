import pgzrun
import random

TITLE="SATELLITE CONNECT"
WIDTH=800
HEIGHT=600

satellitelist=[]

totalsatellites= 7
for i in range(totalsatellites):  
    satellite=Actor("satellite")
    satellite.pos=(random.randint(25,WIDTH-25), random.randint(25,HEIGHT-25))
    satellitelist.append(satellite)

print(satellitelist)
def draw():
    screen.blit("background2", (0,0))
    for satellite in satellitelist:
        satellite.draw()
    

pgzrun.go()