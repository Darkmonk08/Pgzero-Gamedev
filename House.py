import pgzrun

WIDTH=400
HEIGHT=400

def draw():
    house = Rect(100, 150, 200, 150)
    screen.draw.filled_rect(house, (255, 0, 0))
    roof = [(100, 150), (200, 50), (300, 150)]
    screen.draw.line((100,150), (200,50), "green")
    screen.draw.line((100,150), (300,150), "green")
    screen.draw.line((300,150), (200,50), "green")
    screen.draw.filled_circle((350, 50), 30, (255, 255, 0))
    
    
pgzrun.go()
