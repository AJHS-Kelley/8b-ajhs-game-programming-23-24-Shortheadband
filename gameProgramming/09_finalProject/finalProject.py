# FinalProject v0.1 by Gabriel Coffey

# Known Issue List:
#-- Background dosen't fill screen

# Discarded code:

#def retryRes(h,w,resoultion):
#    if resoultion == 1:
#        h = 800
#        w = 600
#    elif resoultion == 2:
#        h = 1920
#        w = 1080
#    elif resoultion == 0:
#        print("Ok")  
#    else:
#        print("This resoultion isn't available")
#        retryRes
 
from ast import Return
import sys, random, math, pygame
from os import listdir
from os.path import isfile, join
pygame.init()

BG_COLOR = (0, 255, 213)
FPS = 60
PLAYER_VEL = 5


resoultion = int(input("(0 for test)Please choose a difficulty. Enter 1 for Low Res or 2 for High Res")) # 0 = LRes(800,600) 1 = HRes(1920,1080)


if resoultion == 1:
    h = 800
    w = 600
elif resoultion == 2:
    h = 1920
    w = 1080
elif resoultion == 0:
    print("Ok")  
else:
    print("This resoultion isn't available")



difficulty = int(input("Please choose a difficulty. Enter 1 for Normal or 2 for Encore"))

if difficulty == 1:
    pygame.display.set_caption('Normal')
elif difficulty == 2:    
    pygame.display.set_caption('Encore')
else:
    print("This resoultion isn't available")

window = pygame.display.set_mode((h,w))

class Player(pygame.sprite.Sprite):
    COLOR = (255,0, 9)
    
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0

    def move(self, dx, dy):
        self.rect.x += dx 
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0
    
    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self,fps):
        self.move(self.x_vel, self.y_vel)

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, self.rect)    

#known Issue -- Background dosen't fill screen
def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(w // width + 1):
        for j in range(h // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image     


def draw(window, background, bg_image, player):
    for tile in background:
        window.blit(bg_image, tile)

    player.draw(window)    

    pygame.display.update()

def handle_move(player):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    if keys[pygame.K_LEFT]:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_VEL)

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")

    player = Player(100,100, 50, 50)

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        player.loop(FPS)    
        handle_move(player)
        draw(window, background, bg_image, player)            
    
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)
    