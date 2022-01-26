import turtle
import random
import copy

screen = turtle.Screen()
turtle.setup(800,800)
turtle.title("Game of Life")
# hide the turtle pointer
turtle.hideturtle()
# no animation because it does not move
turtle.speed(0)
turtle.tracer(0,0)
turtle.pencolor("gray")
turtle.bgcolor("black")

lifeturtle = turtle.Turtle()
lifeturtle.up()
lifeturtle.hideturtle()
lifeturtle.speed(0)

counter = turtle.Turtle()
counter.hideturtle()
counter.speed(0)
counter.color("white")
counter.up()
counter.goto(350,-375)
counter.down()

population = turtle.Turtle()
population.hideturtle()
population.speed(0)
population.color("white")
population.up()
population.goto(-350,-375)
population.down()

fast = turtle.Turtle()
fast.hideturtle()
fast.speed(0)

def draw_grid():
    turtle.pencolor("gray")
    turtle.pensize(1)
    x = -350
    for i in range(n+1):
        draw_line(x,-350,x,350)
        x += 700/n
    y = -350
    for i in range(n+1):
        draw_line(-350,y,350,y)
        y += 700/n

def draw_arrows(x,y):
    fast.up()
    fast.goto(x,y)
    fast.down()
    fast.seth(0)
    fast.color("lightblue")
    fast.begin_fill()
    for i in range(4):
        fast.forward(15)
        fast.left(90)
    fast.end_fill()

# upper arrow
def draw_upper_arrow():
    draw_arrows(50,-370)
    fast.up()
    fast.goto(65,-369)
    fast.down()
    fast.seth(0)
    fast.color("blue")
    fast.begin_fill()
    for i in range(3):
        fast.backward(15)
        fast.right(120)
    fast.end_fill()

# lower arrow
def draw_lower_arrow():
    draw_arrows(-65,-370)
    fast.up()
    fast.goto(-65,-356)
    fast.down()
    fast.seth(0)
    fast.color("blue")
    fast.begin_fill()
    for i in range(3):
        fast.forward(15)
        fast.right(120)
    fast.end_fill()

speed = 1

# draw an nxn grid
n = 50
def draw_line(x1,y1,x2,y2):
    turtle.up()
    turtle.goto(x1,y1)
    turtle.down()
    turtle.goto(x2,y2)

def draw_border():
    turtle.pencolor('gray')
    turtle.pensize(1)
    draw_line(-350,-350,-350,350)
    draw_line(-350,-350,350,-350)
    draw_line(-350,350,350,350)
    draw_line(350,-350,350,350)

# initial screen
# 1/5 probability of each cell to live
life = list()

cont = 0

# draw filled square
def draw_square(x,y,size,status):
    lifeturtle.up()
    lifeturtle.goto(x,y)
    lifeturtle.down()
    lifeturtle.seth(0)
    if status=="t":
        colors_list = ['yellow','white','lightgreen','lightblue','pink']
        lifeturtle.color(random.choice(colors_list))
    elif status=="f":
        lifeturtle.color("black")
    lifeturtle.begin_fill()
    for i in range(4):
        lifeturtle.forward(size)
        lifeturtle.left(90)
    lifeturtle.end_fill()

def draw_life(x,y):
    lx = 700/n*x - 350
    ly = 700/n*y - 350
    draw_square(lx+1, ly+1, 700/n-2,"t")

def draw_all_life():
    global life
    for i in range(n):
        for j in range(n):
            if life[i][j] == 1:
                draw_life(i,j)

def empty_lives():
    global life
    for i in range(n):
        liferow = []
        for j in range(n):
            liferow.append(0)
        life.append(liferow)

def clicked_cell(x,y):
    global life
    if (x < 0):
        x = (-1)*x
        x = (int(x/14)+1)*14
        x = (-1)*x
    else:
        x = int(x/14)*14
    if (y < 0):
        y = (-1)*y
        y = (int(y/14)+1)*14
        y = (-1)*y
    else:
        y = int(y/14)*14
    i = int((x+350)*n/700)
    j = int((y+350)*n/700)
    if life[i][j]==0:
        life[i][j]=1
        draw_square(x+1, y+1, 700/n-2,"t")
    elif life[i][j]==1:
        life[i][j]=0
        draw_square(x+1, y+1, 700/n-2,"f")

def click_func(x,y):
    global speed
    option = "neither"
    if ((x > 50) and (x < 65)) and ((y > -370) and (y < -355)):
        option = "up"
    elif ((x > -65) and (x < -50)) and ((y > -370) and (y < -355)):
        option = "down"
    if (option == "up"):
        if (speed < 9):
            speed += 1
    elif (option == "down"):
        if (speed > 1):
            speed -= 1

def count_neighbors(x,y,screen_life):
    count = 0
    for i in range(3):
        for j in range(3):
            count += screen_life[(x-1+j)%n][(y-1+i)%n]
    if screen_life[x][y] == 1:
        count -= 1
    return count

count_time = 0

def update_life():
    global life
    global count_time
    global speed
    count_pop = 0
    counter.clear()
    population.clear()
    fast.clear()
    newlife = copy.deepcopy(life)
    for i in range(n):
        for j in range(n):
            k = count_neighbors(i,j,life)
            if k < 2 or k > 3:
                newlife[i][j] = 0
            elif k == 3:
                newlife[i][j] = 1
    life = copy.deepcopy(newlife)
    for i in range(n):
        for j in range(n):
            count_pop += life[i][j]
    count_time += 1
    counter.write("Time = " + str(count_time), align="right", font=('Times New Roman', 16, 'normal'))
    population.write("Population = " + str(count_pop), align="left", font=('Times New Roman', 16, 'normal'))
    draw_upper_arrow()
    draw_lower_arrow()
    # draw_arrows(-300,355)
    turtle.onscreenclick(click_func)
    fast.color("white")
    fast.up()
    fast.goto(0, -375)
    fast.down()
    fast.write("Speed = " + str(speed), align="center", font=('Times New Roman', 16, 'normal'))
    lifeturtle.clear()
    draw_all_life()
    screen.update()
    screen.ontimer(update_life,1000-speed*100)

def init_game():
    global life
    turtle.hideturtle()
    turtle.speed(0)
    turtle.tracer(0, 0)
    turtle.pencolor("gray")
    turtle.bgcolor("black")
    draw_grid()
    draw_border()
    fast.color("white")
    fast.up()
    fast.goto(0, -375)
    fast.down()
    fast.write("Press Space to Start Game", align="center", font=('Times New Roman', 16, 'normal'))
    fast.color("white")
    fast.up()
    fast.goto(0, 350)
    fast.down()
    fast.write("Click Cells to Activate or Deactivate", align="center", font=('Times New Roman', 16, 'normal'))
    empty_lives()
    turtle.onscreenclick(clicked_cell)
    turtle.onkeypress(update_life, "space")
    turtle.listen()

init_game()

turtle.done()
