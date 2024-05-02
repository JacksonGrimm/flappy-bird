import pygame 

#Player Class
class player:
    def player_load(screen):
        screen.blit(player_image, (player_x, player_y))


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


#Game screen 
screen = pygame.display.set_mode((800, 600))
running = True
while running:
    
    #Fills screen   
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.player_load(screen)

    pygame.display.update()




        

