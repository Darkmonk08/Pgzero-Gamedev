import pgzrun
import random

WIDTH=600
HEIGHT=600

alien=Actor("alien")
alien.pos=(random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50))
message=""

def draw():
    screen.fill("grey")
    alien.draw()
    screen.draw.text("Shoot the alien", center=(WIDTH/2, 40), fontsize=40, color="black")
    screen.draw.text(message, center=(WIDTH/2, 550), fontsize=40, color="black")


def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        alien.pos=(random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50))
        message="good shot"
    else:
        message="You missed"

    
def update():
    pass

pgzrun.go()