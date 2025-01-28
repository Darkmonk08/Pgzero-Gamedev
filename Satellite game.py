import pgzrun
import random
import time

TITLE="SATELLITE CONNECT"
WIDTH=800
HEIGHT=600

satellitelist=[]
lines=[]
currentsatellite=0
totaltimetaken=0

totalsatellites= 7
for i in range(totalsatellites):  
    satellite=Actor("satellite")
    satellite.pos=(random.randint(25,WIDTH-25), random.randint(25,HEIGHT-25))
    satellitelist.append(satellite)

starttime=time.time()


print(satellitelist)
def draw():
    screen.blit("background2", (0,0))
    number=1
    for satellite in satellitelist:
        satellite.draw()
        screen.draw.text(str(number),(satellite.x+14, satellite.y+12), fontsize=30, color="white")
        number=number+1
    for line in lines:
        screen.draw.line(line[0],line[1], color="White")
    screen.draw.text(str(totaltimetaken), (1,1), fontsize=40, color="Red")
    

def on_mouse_down(pos):
    global currentsatellite
    global lines
    if currentsatellite!=totalsatellites:
        print("done 1")
        if satellitelist[currentsatellite].collidepoint(pos):
            print("done 2")
            if currentsatellite!=0:
                print("Done 3")
                p1=satellitelist[currentsatellite].pos
                p2=satellitelist[currentsatellite-1].pos
                lines.append([p1,p2])
            currentsatellite=currentsatellite+1
        else:
            lines=[]
            currentsatellite=0

def update():
    global totaltimetaken
    if currentsatellite!=totalsatellites:
        totaltimetaken=round(time.time()-starttime)



            



    

pgzrun.go()