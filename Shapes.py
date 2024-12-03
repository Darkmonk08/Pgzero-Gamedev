import pgzrun
import random

WIDTH=400
HEIGHT=400
def draw():
    screen.fill("black")
    for i in range(2,400,20):
        rec=Rect(0,0,i,i)
        rec.center=WIDTH/2,HEIGHT/2
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        screen.draw.rect(rec,(r,g,b))
pgzrun.go()