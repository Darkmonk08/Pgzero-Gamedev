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
totalquestions=0
questionnum=0
question=""
timeleft=3
score=0
gameover=False

def draw():
    if gameover==False:
        screen.fill("Black")
        screen.draw.filled_rect(marqueebox,"black")
        screen.draw.filled_rect(qbox, " dark blue")
        screen.draw.filled_rect(tbox, "green")
        screen.draw.filled_rect(sbox,"red")
        for option in options:
            screen.draw.filled_rect(option,"yellow") 
        
        screen.draw.textbox(f"Welcome to the Quiz! This is Q{questionnum} of {totalquestions}", marqueebox)
        screen.draw.textbox(f"{question[0].strip()}", qbox)
        screen.draw.textbox(f"{question[1].strip()}",qbox1)
        screen.draw.textbox(f"{question[2].strip()}",qbox2)
        screen.draw.textbox(f"{question[3].strip()}",qbox3)
        screen.draw.textbox(f"{question[4].strip()}",qbox4)
        screen.draw.textbox("skip",sbox, angle=90)
        screen.draw.textbox(str(timeleft),tbox, angle=360)
    else:
        screen.fill("black")
        screen.draw.text(f"Your final score is:{score}",(20,20), fontsize=130)
        
                    

def update():
    marqueebox.x=marqueebox.x-1
    if marqueebox.right<=0:
        marqueebox.left=WIDTH


def readquestfile():
    global totalquestions
    openfile=open("questions.txt",'r')
    for statement in openfile:
        statements.append(statement)
    openfile.close()
    totalquestions=len(statements)

def readnextquestion():
    global questionnum, question
    if len(statements)>0:
        questionnum=questionnum+1
        question=statements.pop(0).split("|")
        print(question)
    else:
        gameend()

def on_mouse_down(pos):
    global score
    if sbox.collidepoint(pos):
        readnextquestion()
    for b in options:
        if b.collidepoint(pos):
            if options.index(b)==int(question[5])-1:
                print("correct")
                score=score+1
            readnextquestion()

def updatetimer():
    global timeleft
    if timeleft!=0:
        timeleft=timeleft-1
    else:
        timeleft=3
        readnextquestion()

def gameend():
    global gameover
    gameover=True

clock.schedule_interval(updatetimer,1)

        

readquestfile()
readnextquestion()
pgzrun.go()
