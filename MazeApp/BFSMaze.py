import turtle #For the popup screen
from collections import deque #For the BFS Search

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Breadth-First Search Maze Solver")
screen.setup(1300, 700) #Size of window

#Define the Walls
class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup() #No trail
        self.speed(0) #No animation

class Finish(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

class Next(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

class Start(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
    
class Fastest(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)

#Variables
maze = Maze()
finish = Finish()
start = Start()
next = Next()
fastest = Fastest()
walls = []
path = []
visited = set()
frontier = deque()
solution = {}

grid = [
"++++++++++++++++++++++++++++++++++++++++++++++++++",
"+s   +                      +                    +",
"+  +++  ++++ ++++++   +++++++++++++   +++++ ++++++",
"+    +        +     +                 +          +",
"+ +++++ +++++++++++ +++++++++++++ +++++++++++++  +",
"+        +     +     +         +               + +",
"+ ++++ +++++++ +++++++ +++++ +++++++++++++++++++ +",
"+ +                  +    +           +          +",
"+ +++++++ +++++++++++ +++ +++++++++++ ++++++ +++ +",
"+       +        +    +         +     +          +",
"+++++ +++++++ + ++ ++++++++++++++++ + + ++++++++ +",
"+     +       +     +                          + +",
"+ ++++++++ +++++++ +++++++++++++++++++++++++++++ +",
"+        +             +                         +",
"+ +++++ +++++++++++++++++++++ +++++++++ ++++++++++",
"+ +       +      +        +         +        +   +",
"+ +++++++++++++ ++++++++ ++ + +++++++ ++++++ + +++",
"+          +         +    +        +       + +   +",
"+++++ +++++ +++++ +++  ++++++++++ ++  +++++  ++  +",
"+                         +        +   +         +",
"+ +++++++ ++++++++++++ ++++++ ++++++++++++++ + +++",
"+         +             +               +       e+",
"++++++++++++++++++++++++++++++++++++++++++++++++++"
 ]


def setupMaze(grid):
    global startX, startY, endX, endY
    for y in range(len(grid)): #Read every line in the grid
        for x in range(len(grid[y])): #Read every cell in the grid
            cell = grid[y][x]
            screenX = -575 + (x * 23) #First constant is the offset of middle of the screen, the second constant is the size of the square
            screenY = 275 - (y * 23)

            if cell == "+":
                maze.goto(screenX, screenY) #Move pen towards coordinate
                maze.stamp() #Copy the shape of the maze object to the coordinate
                walls.append((screenX, screenY)) #Add coordinate to walls list
            elif cell == "e":
                finish.goto(screenX, screenY)
                finish.stamp()
                endX, endY = screenX, screenY
            elif cell == "s":
                startX, startY = screenX, screenY
                start.goto(screenX, screenY) #Mark the beginning for the search
            if cell == " " or cell == "e":
                path.append((screenX, screenY)) #Add coordinate to path list

def search(x, y):
    frontier.append((x, y))
    solution[x, y] = x, y
    while len(frontier) > 0: #If there are no blue squares to become explored end the loop
        x, y = frontier.popleft()

        if(x - 23, y) in path and (x - 23, y) not in visited: #Check cell on the left
            cell = (x - 23, y)
            solution[cell] = x, y    #Add the cell (value) from where the current cell (key) came from 
            next.goto(cell)          #Mark the cell in the queue to be searched
            next.stamp()
            frontier.append(cell) #Add cell to frontier list
            visited.add((x - 23, y)) #Add cell to visited list

        if (x, y - 23) in path and (x, y - 23) not in visited: #Check the cell below
            cell = (x, y - 23)
            solution[cell] = x, y
            next.goto(cell)
            next.stamp()
            frontier.append(cell)
            visited.add((x, y - 23))

        if(x + 23, y) in path and (x + 23, y) not in visited: #Check the cell on the right
            cell = (x + 23, y)
            solution[cell] = x, y
            next.goto(cell)
            next.stamp()
            frontier.append(cell)
            visited.add((x + 23, y))

        if(x, y + 23) in path and (x, y + 23) not in visited: #Check the cell above
            cell = (x, y + 23)
            solution[cell] = x, y
            next.goto(cell)
            next.stamp()
            frontier.append(cell)
            visited.add((x, y + 23))
        finish.goto(x, y) #Stamp the square explored
        finish.stamp() 

def backRoute(x, y):
    fastest.goto(x, y) #Stamp the finish square
    fastest.stamp()
    while (x, y) != (startX, startY): #Stop loop when we hit the starting location
        fastest.goto(solution[x, y]) #Stamp the fastest route colour to the solution key
        fastest.stamp()
        x, y = solution[x, y]  #Backtrack where we got the solution from

#Main Program
setupMaze(grid)
search(startX,startY)
backRoute(endX, endY)
screen.exitonclick()
