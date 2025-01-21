import pgzrun
import random

TITLE="BUMBLEBEE VS THE FLOWER"
HEIGHT=500
WIDTH=600
gameover=False

bee=Actor("bee")
bee.pos=(random.randint(50,WIDTH-50), random.randint(50,HEIGHT-50))
flower=Actor("flower")
flower.pos=(random.randint(50,WIDTH-50), random.randint(50,HEIGHT-50))
score=0
 #screen.draw.text("Shoot the alien", center=(WIDTH/2, 40), fontsize=40, color="black")
def draw():
    if gameover==False:
        screen.blit("background", (0,0))
        bee.draw()
        flower.draw()
        screen.draw.text("Score:"+str(score),(1,1), fontsize=30, color="black")
    else:
        screen.fill("Blue")
        screen.draw.text("Game over, your score was "+str(score),(10,10), fontsize=60, color="black")
        

def gameend():
    global gameover
    gameover=True


'''def on_key_down(key):
    if key==keys.RIGHT:
        bee.x=bee.x+4'''
    #because you have to repitialy press the button for it to move
  
def update():
    global score
    if keyboard.right:
        bee.x=bee.x+4
    if keyboard.left:
        bee.x=bee.x-4
    if keyboard.up:
        bee.y=bee.y-4
    if keyboard.down:
        bee.y=bee.y+4
    if bee.colliderect(flower):
        flower.pos=(random.randint(50,WIDTH-50), random.randint(50,HEIGHT-50))
        score=score+1
    
clock.schedule(gameend, 30)



pgzrun.go()
