import pygame 
from player import Player


#Initializes pygame
pygame.init()

#Game Caption
pygame.display.set_caption("Flappy Bird")

#Window icon set to a bird
game_icon = pygame.image.load("flappybird.png")
pygame.display.set_icon(game_icon)

#Player
player_image = pygame.image.load("flappybird.png")
player_x = 370
player_y = 480

bird = Player(player_image, player_x, player_y)


#Game screen 
screen = pygame.display.set_mode((800, 600))
running = True
while running:
    
    #Fills screen   
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    bird.player_load(screen)

    pygame.display.update()




        

