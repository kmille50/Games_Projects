import turtle
import random

# Initialization of game's variables
w = 500
h = 500
food_size = 10
delay = 100

offsets = {
    "haut":(0,20),
    "bas":(0,-20),
    "gauche":(-20,0),
    "droite":(20,0)
}

def reset():
    global snake, snake_dir, food_position, pen
    snake = [[0,0], [0,20],[0,40],[0,60], [0,80]]
    snake_dir = "up"
    food_position = get_random_food_position()
    food.goto(food_position)
    move_snake()

def move_snake():
    global snake_dir

    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snake_dir][0]
    new_head[1] = snake[-1][1] + offsets[snake_dir][1]

    if new_head in snake[:-1]:
        reset()
    else:
        snake.append(new_head)

        if not food_collision():
            snake.pop(0)

        if snake[-1][0] > w / 2:
            snake[-1][0] -= w
        elif snake[-1][0] < - w / 2:
            snake[-1][0] += w
        elif snake[-1][1] > h / 2:
            snake[-1][1] -= h
        elif snake[-1][1] < -h / 2:
            snake[-1][1] += h

        pen.clearstamps()

        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()

        screen.update
        turtle.ontimer(move_snake,delay)

# Collision food and snake
def food_collision():
    global food_collision
    if get_distance(snake[-1], food_position) < 20:
        food_position = get_random_food_position()
        food.goto(food_position)
        return True
    return False

# Draw blocs of food randomly in the field
def get_random_food_position():
    x = random.randint(- w / 2 + food_size, w / 2 - food_size)
    y = random.randint(- h / 2 + food_size, h / 2 - food_size)
    return (x, y)

# Move of the snake
def get_distance (pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2 
    distance = ((y2-y1) ** 2 + (x2-x1) ** 2) ** 0.5
    return distance 

def go_up():
    global snake_dir
    if snake_dir != "down":
        snake_dir = "up"

def go_right():
    global snake_dir
    if snake_dir != "left":
        snake_dir = "right"

def go_down():
    global snake_dir
    if snake_dir != "up":
        snake_dir = "down"

def go_left():
    global snake_dir
    if snake_dir != "right":
        snake_dir = "left"


# Set up the screen
screen = turtle.Screen()
screen.setup(width=500, height=500)
screen.title("Snake")
screen.bgcolor("blue")
screen.tracer(0) # Turns off the screen updates

pen = turtle.Turtle("square")
pen.penup()

food = turtle.Turtle()
food.shape("square")
food.color("yellow")
food.shapesize(food_size / 20)
food.penup()

# Move player
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

reset()
turtle.done()