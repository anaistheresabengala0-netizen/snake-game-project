
import pygame
from pygame.math import Vector2

li = pygame.init()

WIDTH = 600
HEIGHT = 600

cell = 20
cell_num = 25
# screen = pygame.display.set_mode((cell*cell_num,cell*cell_num))
screen = pygame.display.set_mode((WIDTH,HEIGHT))
apple = pygame.image.load('appa.png').convert_alpha()#loads image from code folder and convert it to a python-friendly format
apple = pygame.transform.scale(apple, (cell-1,cell-1))# resize image
apple_rot = pygame.image.load('applerot.png').convert_alpha()
apple_rot = pygame.transform.scale(apple_rot, (cell-1,cell-1))
clock = pygame.time.Clock()

running = True 

class Food:
    def __init__(self):

        # food position
        self.position = Vector2(5,6)
    def draw(self):
        #food_rect = pygame.Rect(self.position.x*cell,
                                #self.position.y*cell,
                                #cell,
                                #cell
        #)
        # center of the grid
        x = int(self.position.x * cell + cell / 2)
        y = int(self.position.y * cell + cell / 2)
        food_rect = apple.get_rect(center = (x, y))
        screen.blit(apple,food_rect)
        pass

class Poison:
    def __init__(self):

        # food position
        self.position = Vector2(9,6)
    def draw(self):
        food_rect = pygame.Rect(self.position.x*cell,self.position.y*cell,cell,cell)
        screen.blit(apple_rot,food_rect)
        pass



def grid_lines():
    """for y in range(0,HEIGHT,20):
        pygame.draw.line(screen,"yellow2",(0,y), (WIDTH, y ))
    for x in range(0,WIDTH,20):
        pygame.draw.line(screen, 'yellow2',(x,0),(x,HEIGHT))
    pygame.display.flip()"""

    # Drawing lines 
    for y in range(0,HEIGHT,cell):
        for x in range(0, WIDTH, cell):
            rect = pygame.Rect(x,y,cell,cell)
            # filling boxes created by intersection of the lines 
            if(x// cell + y // cell) % 2 ==0:# Alternating colours to have a checkerboard effect
                pygame.draw.rect(screen,'olivedrab2',rect)
            else:
                pygame.draw.rect(screen,'olivedrab3',rect)
    pass


class Snake:
    def __init__(self):
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]# snake initial position

    def draw(self):
        for segment in self.body:
            segment_rect = (segment.x * cell, segment.y * cell, cell, cell)# making the snake rectangular (x,y,width,height)
            pygame.draw.rect(screen, "indigo", segment_rect)
        pass

snake = Snake()

food = Food()

poison = Poison()
# food_surface = pygame.image.load('apple.png')

grid_lines()

while running:
    # this is the game loop that pools for events
    # the pygame.QUIT event means the user clicked x to close the window. 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #visual elements
    screen.fill("aquamarine3")#yill the screen with a color to wipe away anything from last fram. 
    grid_lines()
    snake.draw()
    food.draw()
    poison.draw()
    # here we can render the game here. 


    pygame.display.flip() # flip th display to put your work on the screen
    clock.tick(60)

pygame.quit()


"""

The way pygame funstions 

1- first we initialise the pygame after importing it
2- create the the screen  using the display.setmode 
3- create and infinite loop and mae it stop wen the user clikcs the x, using the pygame.quit
4- use screen,fill to overwirte everything on the screen, finalyy use display.flip to put your work on the screen. 



"""

