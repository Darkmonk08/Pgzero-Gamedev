import pgzrun

WIDTH=1000
HEIGHT=750
statements=[]
marqueebox=Rect(0,0,1000,50)
qbox=Rect(10,60,700, 260)
tbox=Rect(720,60, 270, 260)
qbox1=Rect(10,330,345,200)
qbox2=Rect(10,540,345,200)
qbox3=Rect(365,330,345,200)
qbox4=Rect(365,540,345,200)
sbox=Rect(720,330,270, 410)
options=[qbox1,qbox2,qbox3,qbox4]

def draw():
    screen.fill("Black")
    screen.draw.filled_rect(marqueebox,"black")
    screen.draw.filled_rect(qbox, " dark blue")
    screen.draw.filled_rect(tbox, "green")
    screen.draw.filled_rect(sbox,"red")
    for option in options:
        screen.draw.filled_rect(option,"yellow") 
    
    screen.draw.textbox("Welcome to the Quiz! This is Q_ of _", marqueebox)
                    

def update():
    pass


def readquestfile():
    openfile=open("questions.txt",'r')
    for statement in openfile:
        statements.append(statement)
    openfile.close()

readquestfile()
print(statements)
pgzrun.go()