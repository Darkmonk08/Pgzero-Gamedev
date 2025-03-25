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

def draw():
    screen.fill("black")
    apple.draw()
    screen.draw.text("Score:"+str(score),center=(WIDTH/2, 40), fontsize=60, color="white")
    snake.draw()
    if gamefinish==True:
        screen.fill("Red")
        screen.draw.text("Game over", center=(WIDTH/2,30), fontsize=90, color="black")
        screen.draw.text("Your final score was:"+ str(score),center=(WIDTH/2, 90), fontsize=80, color="black")
    

def update():
    global score
    global speed
    if keyboard.right:
        snake.x=snake.x+speed
    if keyboard.left:
        snake.x=snake.x-speed
    if keyboard.up:
        snake.y=snake.y-speed
    if keyboard.down:
        snake.y=snake.y+speed

    if snake.colliderect(apple):
        apple.pos=(random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50))
        score=score+1
    if snake.x>=WIDTH or snake.y>=HEIGHT or snake.x<=0 or snake.y<=0:
        gameover()
    if score!=0 and score%10==0:
        speed=speed+5
        

def gameover():
    global gamefinish
    gamefinish=True

    






pgzrun.go()