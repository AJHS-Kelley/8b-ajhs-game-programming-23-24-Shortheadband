# FinalProject v0.1 by Gabriel Coffey

# Known Issue List:
#-- Background dosen't fill screen
#-- 3 New Errors(Crash code)

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

def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))] #Error

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))
        
        if direction:
            all_sprites[image.replace(".png," "") + "_right"] = sprites # Error
            all_sprites[image.replace(".png," "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites
    
    return all_sprites 


class Player(pygame.sprite.Sprite): #Error
    COLOR = (255,0, 9)
    GRAVITY = 1
    SPRITES = load_sprite_sheets("MainCharacters", "MaskDude", 32, 32, True) 
    
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0

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
        #self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)

        self.fall_count += 1

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, self.rect)   
        self.sprite = self.SPRITES["idle_" + self.direction][0]
        win.blit(self.sprite, (self.rect.x, self.rect.y)) 

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
    