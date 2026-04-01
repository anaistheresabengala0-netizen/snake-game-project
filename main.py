
import pygame
from pygame.math import Vector2

li = pygame.init()

cell = 30
cell_num = 25
screen = pygame.display.set_mode((cell*cell_num,cell*cell_num))



clock = pygame.time.Clock()

running = True 

class Food:
    def __init__(self):

        # food position
        self.position = Vector2(5,6)
    def draw(self):
        food_rect = pygame.Rect(self.position.x*cell,self.position.y*cell,cell,cell)
        # screen.blit(food_surface,food_rect)
        pass


def grid_lines():

    pass

food = Food()
# food_surface = pygame.image.load('apple.png')


while running:
    # this is the game loop that pools for events
    # the pygame.QUIT event means the user clicked x to close the window. 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #visual elements
    screen.fill("aquamarine3")#yill the screen with a color to wipe away anything from last fram. 
    food.draw()


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

