import pygame 
from player import Player


#Initializes pygame
pygame.init()
dt = 1
clock = pygame.time.Clock()

#Game Caption
pygame.display.set_caption("Flappy Bird")

#Window icon set to a bird
game_icon = pygame.image.load("flappybird.png")
pygame.display.set_icon(game_icon)

#Player
player_image = pygame.image.load("flappybird.png")
player_image = pygame.transform.scale(player_image, (50, 50))
player_x = 200
player_y = 30
bird = Player(player_image, player_x, player_y)


#Game screen 
screen = pygame.display.set_mode((800, 600))
running = True
start_drop = False


while running:
    keys = pygame.key.get_pressed()
    
    #Fills screen   
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    bird.player_load(screen)

    
    if(keys[pygame.K_w]):
        start_drop = True
        bird.update_y(-600, dt)
        
 

    if(start_drop):
     bird.update_y(150, dt)
     
    pygame.display.flip()
    dt = clock.tick(60) / 1000



        

