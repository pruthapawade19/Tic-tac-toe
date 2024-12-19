import turtle as t
w = t.Screen()
w.bgcolor("black")

b = t.Turtle()
t1 = t.Turtle()
t1.color("white")
t1.lt(90)
b.color("white")
t1.speed(0)
b.pu()
b.goto(-150,150)
b.pd()
b.speed(0)

def start():
    global tog,pos,box1,box2,box3,box4,box5,box6,box7,box8,box9,row1,row2,row3
    global col1,col2,col3,dia1,dia2,circle_won,cross_won
    tog = 0
    box1  = 0
    box2  = 0
    box3  = 0
    box4  = 0
    box5  = 0
    box6  = 0
    box7  = 0
    box8  = 0
    box9  = 0
    row1 = []
    row2 = []
    row3 = []
    col1 = []
    col2 = []
    col3 = []
    dia1 = []
    dia2 = []
    circle_won = 0
    cross_won = 0
def draw(x,y):
    global tog,pos,box1,box2,box3,box4,box5,box6,box7,box8,box9,circle_won,cross_won
    print(x,y)

    if(-290 < x < -190 and -20 < y < 50):
        t1.reset()
        t1.lt(90)
        t1.color("white")
        t1.speed(0)
        start()
        
    if(-150 < x < -50 and 50 < y < 150 and box1 == 0):   #1
        pos = (-130,100)
        box1 = 1
        if(tog == 0):
            row1.append(0)
            col1.append(0)
            dia1.append(0)
        else:
            row1.append(1)
            col1.append(1)
            dia1.append(1)
            
        cir_cross()
        
    if(-50 < x < 50 and 50 < y < 150 and box2 == 0):    #2
        pos = (-30,100)
        box2 = 1
        if(tog == 0):
            row1.append(0)
            col2.append(0)
            
        else:
            row1.append(1)
            col2.append(1)
           
        cir_cross()

    if(50 < x < 150 and 50 < y < 150 and box3 == 0):   #3
        pos = (70,100)
        box3 = 1
        if(tog == 0):
            row1.append(0)
            col3.append(0)
            dia2.append(0)
        else:
            row1.append(1)
            col3.append(1)
            dia2.append(1)
        cir_cross()

    if(-150 < x < -50 and -50 < y < 50 and box4 == 0):   #4
        pos = (-130,0)
        box4 = 1
        if(tog == 0):
            row2.append(0)
            col1.append(0)
            
        else:
            row2.append(1)
            col1.append(1)
          
        cir_cross()
        
    if(-50 < x < 50 and -50 < y < 50 and box5 == 0):    #5
        pos = (-30,0)
        box5 = 1
        if(tog == 0):
            row2.append(0)
            col2.append(0)
            dia1.append(0)
            dia2.append(0)
        else:
            row2.append(1)
            col2.append(1)
            dia1.append(1)
            dia2.append(1)
        cir_cross()

    if(50 < x < 150 and -50 < y < 50 and box6 == 0):   #6
        pos = (70,0)
        box6 = 1
        if(tog == 0):
            row2.append(0)
            col3.append(0)
            
        else:
            row2.append(1)
            col3.append(1)
            
        cir_cross()    

    if(-150 < x < -50 and -150 < y < -50 and box7 == 0):   #7
        pos = (-130,-100)
        box7 = 1
        if(tog == 0):
            row3.append(0)
            col1.append(0)
            dia2.append(0)
        else:
            row3.append(1)
            col1.append(1)
            dia2.append(1)
        cir_cross()
        
    if(-50 < x < 50 and -150 < y < -50 and box8 == 0):    #8
        pos = (-30,-100)
        box8 = 1
        if(tog == 0):
            row3.append(0)
            col2.append(0)
           
        else:
            row3.append(1)
            col2.append(1)
            
        cir_cross()

    if(50 < x < 150 and -150 < y < -50 and box9 == 0):   #9
        pos = (70,-100)
        box9 = 1
        if(tog == 0):
            row3.append(0)
            col3.append(0)
            dia1.append(0)
        else:
            row3.append(1)
            col3.append(1)
            dia1.append(1)
        cir_cross() 

    print('row1 = ',row1)
    print('row2 = ',row2)
    print('row3 = ',row3)
    print('col1 = ',col1)
    print('col2 = ',col2)
    print('col3 = ',col3)
    print('dia1 = ',dia1)
    print('dia2 = ',dia2)

    if(len(row1) == 3):
        if(row1[0] == row1[1] == row1[2]):
            draw_line((-145,100),90,t1,290)
            if(row1[0] == 0):
                print("Circle won")
                circle_won = 1
            else:
                print("Cross won")
                cross_won = 1
                
    if(len(row2) == 3):
        if(row2[0] == row2[1] == row2[2]):
            draw_line((-145,0),90,t1,290)
            if(row2[0] == 0):
                print("Circle won")
                circle_won = 1
            else:
                print("Cross won")
                cross_won = 1

    if(len(row3) == 3):
        if(row3[0] == row3[1] == row3[2]):
            draw_line((-145,-100),90,t1,290)
            if(row3[0] == 0):
                print("Circle won")
                circle_won = 1
            else:
                print("Cross won")
                cross_won = 1

    if(len(col1) == 3):
        if(col1[0] == col1[1] == col1[2]):
            draw_line((-100,145),180,t1,290)
            if(col1[0] == 0):
                print("Circle won")
                circle_won = 1
            else:
                print("Cross won")
                cross_won = 1

    if(len(col2) == 3):
        if(col2[0] == col2[1] == col2[2]):
            draw_line((0,145),180,t1,290)
            if(col2[0] == 0):
                print("Circle won")
                circle_won = 1
            else:
                print("Cross won")
                cross_won = 1

    if(len(col3) == 3):
        if(col3[0] == col3[1] == col3[2]):
            draw_line((100,145),180,t1,290)
            if(col3[0] == 0):
                print("Circle won")
                circle_won = 1
            else:
                print("Circle won")
                cross_won = 1

    if(len(dia1) == 3):
        if(dia1[0] == dia1[1] == dia1[2]):
            draw_line((-145,145),135,t1,415)
            if(dia1[0] == 0):
                print("Circle won")
                circle_won = 1
            else:
                print("Cross won")
                cross_won = 1

    if(len(dia2) == 3):
        if(dia2[0] == dia2[1] == dia2[2]):
            draw_line((145,145),225,t1,415)
            if(dia2[0] == 0):
                print("Circle won")
                circle_won = 1
            else:
                print("Cross won")
                cross_won = 1
    if(len(row1) == 3 and len(row2) == 3 and len(row3) == 3 and
       len(col1) == 3 and len(col2) == 3 and len(col3) == 3 and len(dia1) == 3 and
       len(dia2) == 3 and circle_won == 0 and cross_won == 0):
           t1.pu()
           t1.goto(-135,-250)
           t1.pd()
           t1.color('red')
           t1.write("Match Tie", font = ("Arial",34))
           
    if(circle_won == 1):
        t1.pu()
        t1.goto(-135,-250)
        t1.pd()
        t1.color('green2')
        t1.write("Circle_won", font = ("Arial",34))
    if(cross_won == 1):
        t1.pu()
        t1.goto(-135,-250)
        t1.pd()
        t1.color('green2')
        t1.write("Cross_won", font = ("Arial",34))    
        


def cir_cross():
    global tog,pos
    if(tog == 0):
            draw_circle(pos)
            tog = 1
    else:
            draw_cross(pos)
            tog = 0

def draw_line(pos,angle,turt,dist):
    turt.pu()
    turt.goto(pos)
    turt.rt(angle)    
    turt.pd()
    turt.fd(dist)

def draw_circle(pos):
    t1.pu()
    t1.goto(pos)
    t1.pd()
    t1.begin_fill()
    t1.circle(-30)
    t1.end_fill()
    
def draw_cross(pos):
    x,y = pos
    x = x+5
    y += 25
    t1.pensize(2)
    draw_line((x,y),135,t1,70)
    t1.pu()
    y -= 50
    draw_line((x,y),270,t1,70)
    t1.lt(45)

for i in range(4):
    b.fd(300)
    b.rt(90)

draw_line((-150,50),0,b,300)
draw_line((-150,-50),0,b,300)
draw_line((-50,150),90,b,300)
draw_line((50,150),0,b,300)

b.pu()
b.goto(-170,200)
b.pd()
b.write("Tic Tac Toe Game", font= ("Arial",34))

b.pu()
b.goto(-290,50)
b.color("yellow")
b.pd()
b.lt(90)
b.begin_fill()
for i in range(2):
    b.fd(100)
    b.rt(90)
    b.fd(70)
    b.rt(90)
b.end_fill()

b.color("black")
b.pu()
b.goto(-270,20)
b.write("Click to", font = ("Arial",14))
b.goto(-260,0)
b.write("Start", font = ("Arial",14))
b.hideturtle()   

w.onscreenclick(draw)
t.done()