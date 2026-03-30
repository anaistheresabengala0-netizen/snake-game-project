
import pygame


li = pygame.init()

screen = pygame.display.set_mode((800,800))



clock = pygame.time.Clock()

running = True 


while running:
    # this is the game loop that pools for events
    # the pygame.QUIT event means the user clicked x to close the window. 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("blue")#yill the screen with a color to wipe away anything from last fram. 

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

