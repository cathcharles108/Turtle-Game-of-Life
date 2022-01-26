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

# draw an nxn grid
n = 50
def draw_line(x1,y1,x2,y2):
    turtle.up()
    turtle.goto(x1,y1)
    turtle.down()
    turtle.goto(x2,y2)

def draw_border():
    turtle.pencolor('gray')
    turtle.pensize(3)
    draw_line(-350,-350,-350,350)
    draw_line(-350,-350,350,-350)
    draw_line(-350,350,350,350)
    draw_line(350,-350,350,350)

# initial screen
# 1/5 probability of each cell to live
life = list()

def init_lives():
    for i in range(n):
        liferow = []
        for j in range(n):
            if random.randint(0,5) == 0:
                liferow.append(1)
            else:
                liferow.append(0)
        life.append(liferow)

# draw filled square
def draw_square(x,y,size):
    lifeturtle.up()
    lifeturtle.goto(x,y)
    lifeturtle.down()
    lifeturtle.seth(0)
    lifeturtle.begin_fill()
    for i in range(4):
        lifeturtle.forward(size)
        lifeturtle.left(90)
    lifeturtle.end_fill()
    colors_list = ['yellow','white','lightgreen','lightblue','pink']
    lifeturtle.color(random.choice(colors_list))

def draw_life(x,y):
    lx = 700/n*x - 350
    ly = 700/n*y - 350
    draw_square(lx+1, ly+1, 700/n-2)

def draw_all_life():
    global life
    for i in range(n):
        for j in range(n):
            if life[i][j] == 1:
                draw_life(i,j)

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
    count_pop = 0
    counter.clear()
    population.clear()
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
    lifeturtle.clear()
    draw_all_life()
    screen.update()
    screen.ontimer(update_life,300)

draw_border()
init_lives()
update_life()

turtle.done()
