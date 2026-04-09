import pygame, random, time
from pygame.math import Vector2

li = pygame.init()
scene = "MENU"
current_speed = 5
current_level = "EASY"

WIDTH = 800
HEIGHT = 800

cell = 20
cell_num = 25
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#loads image from code folder and convert it to a python-friendly format
apple = pygame.image.load('appa.png').convert_alpha()
apple_rot = pygame.image.load('poison.png').convert_alpha()

# resize image to fit in grid
apple = pygame.transform.scale(apple, (cell-1,cell-1))
apple_rot = pygame.transform.scale(apple_rot, (cell-1,cell-1))
clock = pygame.time.Clock()

running = True 

class Food:
    def __init__(self):
        # food position
        self.position = self.random_position()

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

    def random_position(self):
        x = random.randint(0, cell_num - 1)
        y = random.randint(0, cell_num - 1)
        position = Vector2(x,y)
        return position
        pass
food = Food()



class Poison:
    def __init__(self):

        # food position
        self.position = self.random_position()
    def draw(self):
        food_rect = pygame.Rect(self.position.x*cell,self.position.y*cell,cell,cell)
        screen.blit(apple_rot,food_rect)
        
    
    def random_position(self):
        x = random.randint(0, cell_num - 1)
        y = random.randint(0, cell_num - 1)
        position = Vector2(x,y)
        return position
        pass

poison = Poison()




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



class Button:
    def __init__(self, text, x, y, width, height, color, hover_color):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.SysFont("Arial", 30)

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        
        pygame.draw.rect(surface, current_color, self.rect, border_radius=15)
   
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False




btn_easy = Button("EASY", 300, 200, 200, 60, (50, 150, 50), (70, 210, 70))
btn_med  = Button("MEDIUM", 300, 300, 200, 60, (200, 150, 0), (240, 190, 0))
btn_hard = Button("HARD", 300, 400, 200, 60, (150, 50, 50), (210, 70, 70))



def get_level_and_speed(event):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if btn_easy.is_clicked(event):
            return {"level": "EASY", "speed": 5}
        if btn_med.is_clicked(event):
            return {"level": "MEDIUM", "speed": 10}
        if btn_hard.is_clicked(event):
            return {"level": "HARD", "speed": 15}
    return None


class Snake:
    def __init__(self):
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
        self.direction = Vector2(1,0)
        self.add = False
        self.speed = 5


    def draw(self):
        for segment in self.body:
            segment_rect = (segment.x * cell, segment.y * cell, cell, cell)# making the snake rectangular (x,y,width,height)
            pygame.draw.rect(screen, "indigo", segment_rect)
        
    
    def move(self):
        new_head = self.body[0] + self.direction
        self.body.insert(0, new_head)
        if self.add:
            self.add = False
        else:
            self.body.pop()  
    
    def move_right(self):
        self.direction = Vector2(1, 0)

    def move_left(self):
        self.direction = Vector2(-1, 0)

    def move_up(self):
        self.direction = Vector2(0, -1)

    def move_down(self):
        self.direction = Vector2(0, 1)
    
    


snake = Snake()
# snake.draw()




def track_key_press():
    key_press = pygame.key.get_pressed()
    if key_press[pygame.K_LEFT]:
        snake.move_left()
    if key_press[pygame.K_RIGHT]:
        snake.move_right()
    if key_press[pygame.K_UP]:
        snake.move_up()
    if key_press[pygame.K_DOWN]:
        snake.move_down()
    if key_press[pygame.K_SPACE]:
        print("Space key pressed")



    
class Collisions():
    def __init__(self,snake,food,poison):
        self.snake = snake
        self.food = food
        self.poison = poison
        self.food_collision()
    
    def food_collision(self):
       if self.snake.body[0] == self.food.position:
        self.food.position = self.food.random_position()
        self.snake.add = True
    
    def poison_collision(self):
        if self.snake.body[0] == self.poison.position:
            self.poison.position = self.poison.random_position()

            if len(self.snake.body) > 1:
                self.snake.body.pop()

    pass 

    
coll = Collisions(snake,food,poison)



# food_surface = pygame.image.load('apple.png')

grid_lines()

while running:
    # this is the game loop that pools for events
    # the pygame.QUIT event means the user clicked x to close the window. 
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if scene == "MENU":
            result = get_level_and_speed(event)
            if result is not None:
                current_level = result["level"]
                current_speed = result["speed"]
                snake.speed = current_speed
                scene = "GAME"
        elif scene == "GAME":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                scene = "MENU"


    #visual elements
   
    screen.fill("aquamarine3")#yill the screen with a color to wipe away anything from last fram. 
    if scene == "MENU":
        btn_easy.draw(screen)
        btn_med.draw(screen)
        btn_hard.draw(screen)
    elif scene == "GAME":
        grid_lines()
        snake.draw()
        food.draw()
        poison.draw()
        track_key_press()
        snake.move()
        coll.food_collision()
        coll.poison_collision()
    pygame.display.flip() # flip th display to put your work on the screen
    clock.tick(snake.speed)

pygame.quit()


"""

The way pygame funstions 

1- first we initialise the pygame after importing it
2- create the the screen  using the display.setmode 
3- create and infinite loop and mae it stop wen the user clikcs the x, using the pygame.quit
4- use screen,fill to overwirte everything on the screen, finalyy use display.flip to put your work on the screen. 



"""

