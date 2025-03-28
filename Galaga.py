import pgzrun

WIDTH=1400
HEIGHT=900

galaga=Actor("galaga")
galaga.pos=(WIDTH/2,HEIGHT-50)
bullets=[]
enemeys=[]
xpos=25
ypos=25
score=0
direction=1
down=False
gameover=False

for i in range(3):
    row=[]
    for i in range(3):
        enemey=Actor("galagaenemy")
        enemey.pos=(xpos,ypos)
        row.append(enemey)
        xpos=xpos+70
    enemeys.append(row)
    ypos=ypos+50
    xpos=25
        
print(enemeys)
def draw():
    if gameover==False:
        screen.fill("Black")
        galaga.draw()
        for bullet in bullets:
            bullet.draw()
        for enemey in enemeys:
            for i in enemey:
                i.draw()
        screen.draw.text("Score:"+str(score),(WIDTH-100,HEIGHT-100), fontsize=30, color="white")
    else:
        screen.fill("Red")
        screen.draw.text("Gamover, your score was1"+str(score),(300,200), fontsize=100, color="black")



def on_key_down(key):
    if key==keys.SPACE:
        bullet=Actor("bullet")
        bullet.pos=(galaga.x, galaga.y)
        bullets.append(bullet)


        


def update():
    global score
    global direction
    global down
    global gameover
    if keyboard.right and galaga.x!=WIDTH:
        galaga.x=galaga.x+5
    if keyboard.left and galaga.x!=0:
        galaga.x=galaga.x-5
    for bullet in bullets:
        if bullet.y>0:
            bullet.y=bullet.y-10
        else:
            bullets.remove(bullet)
    #checking for enemy and bullet collision
    for i in range(len(enemeys)): 
        for enemey in enemeys[i]:
            for bullet in bullets:
                if bullet.colliderect(enemey):
                    enemeys[i].remove(enemey)
                    bullets.remove(bullet)
                    score=score+1
    #moving the enemey
    movedown=False
    if len(enemeys)>0 and (enemeys[0][-1].x>=WIDTH or enemeys[0][0].x<=0):
        direction=direction*-1
        movedown=True
    for enemey in enemeys:
        for i in enemey:
            i.x=i.x+50*direction
            if movedown==True:
                i.y=i.y+50
                down=True
    if down==True:
        enemeyrow=[]
        if direction==1:
            xposi=0
        else:
            xposi=WIDTH
        yposi=30
        for i in range(3):
            newenemey=Actor("galagaenemy")
            newenemey.pos=(xposi,yposi)
            xposi=xposi+(70*direction) 
            enemeyrow.append(newenemey)
        enemeys.append(enemeyrow)
        print(enemeys)        
        down=False
    #checking for enemey galaga collision
    for i in range(len(enemeys)):
        for enemey in enemeys[i]:
            if galaga.colliderect(enemey):
                gameover=True


    




pgzrun.go()
