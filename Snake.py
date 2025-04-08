import pgzrun
import random

WIDTH=1000
HEIGHT=800

apple=Actor("apple")
apple.pos=(random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50))
snake=Actor("snake head")
snake.pos=(WIDTH/2,HEIGHT/2)
speed=3
score=0
gamefinish=False
movement={"up":False,"down":False,"right":False,"left":False}
bodypart=[]

def draw():
    screen.fill("black")
    apple.draw()
    screen.draw.text("Score:"+str(score),center=(WIDTH/2, 40), fontsize=60, color="white")
    for i in bodypart:
        i.draw()
    snake.draw()
    if gamefinish==True:
        screen.fill("Red")
        screen.draw.text("Game over", center=(WIDTH/2,30), fontsize=90, color="black")
        screen.draw.text("Your final score was:"+ str(score),center=(WIDTH/2, 90), fontsize=80, color="black")
    

def update():
    bodymovementx=0
    bodymovementy=0
    global score
    global speed
    if movement["right"]:
        snake.x=snake.x+speed
        bodymovementx=-60
    if movement["left"]:
        snake.x=snake.x-speed
        bodymovementx=60
    if movement["up"]:
        snake.y=snake.y-speed
        bodymovementy=60
    if movement["down"]:
        bodymovementy=-60
        snake.y=snake.y+speed
    
    if len(bodypart)>0:
            bodypart[0].pos=snake.x+bodymovementx,snake.y+bodymovementy
            for i in range(1,len(bodypart)):
                bodypart[i].pos=bodypart[i-1].x+bodymovementx,bodypart[i-1].y+bodymovementy

            

    if snake.colliderect(apple):
        apple.pos=(random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50))
        score=score+1
        body=Actor("snake body" ) 
        bodypart.append(body)
    if snake.x>=WIDTH or snake.y>=HEIGHT or snake.x<=0 or snake.y<=0:
        gameover()
    
def on_key_down(key):
    movement["right"]=False
    movement["left"]=False
    movement["up"]=False
    movement["down"]=False
    if key==keys.RIGHT:
        movement["right"]=True
    if key==keys.LEFT:
        movement["left"]=True
    if key==keys.UP:
        movement["up"]=True
    if key==keys.DOWN:
        movement["down"]=True

def gameover():
    global gamefinish
    gamefinish=True

    






pgzrun.go()
