#Player Class
class Player:
    def __init__(this, player_image, player_x, player_y):
            this.image = player_image
            this.x = player_x
            this.y = player_y
        
    def player_load(this, screen):
        screen.blit(this.image, (this.x, this.y))
