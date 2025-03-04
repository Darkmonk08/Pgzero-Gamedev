import pgzrun

WIDTH=1400
HEIGHT=900

galaga=Actor("galaga")
galaga.pos=(WIDTH/2,HEIGHT-50)
bullets=[]
enemeys=[]
for i in range(3):
    row=[]
    for i in range(3):
        enemey=Actor("galagaenemy")
        row.append(enemey)
    enemeys.append(row)
print(enemeys)
def draw():
    screen.fill("Black")
    galaga.draw()
    for bullet in bullets:
        bullet.draw()



def on_key_down(key):
    if key==keys.SPACE:
        bullet=Actor("bullet")
        bullet.pos=(galaga.x, galaga.y)
        bullets.append(bullet)


        


def update():
    if keyboard.right and galaga.x!=WIDTH:
        galaga.x=galaga.x+5
    if keyboard.left and galaga.x!=0:
        galaga.x=galaga.x-5
    for bullet in bullets:
        if bullet.y>0:
            bullet.y=bullet.y-10
        else:
            bullets.remove(bullet)



pgzrun.go()