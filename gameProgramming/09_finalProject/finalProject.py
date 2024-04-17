# FinalProject v0.0 by Gabriel Coffey
import sys, random, math, pygame
from os import listdir
from os.path import isfile, join
pygame.init()

BG_COLOR = (0, 255, 213)
FPS = 60
PLAYER_VEL = 5

resoultion = int(input("Please choose a difficulty. Enter 1 for Low Res or 2 for High Res")) # 0 = LRes(800,600) 1 = HRes(1920,1080)

if resoultion == 1:
    h = 800
    w = 600
elif resoultion == 2:
    h = 1920
    w = 1080
else: print("This resoultion isn't available")  


difficulty = int(input("Please choose a difficulty. Enter 1 for Normal or 2 for Encore"))

if difficulty == 1:
    pygame.display.set_caption('Normal')
else:    
    pygame.display.set_caption('Encore')

window = pygame.display.set_mode((h,w))

class Player(pygame.sprite.sprite):
    

def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    x, y, _, _ = image.get_rect()
    tiles = []

    for i in range(w // width + 1):
        for j in range(h // height + 1):
            pos = [i * width, j * height]
            tiles.append (pos)

    return tiles, image        

def draw(window,background):
    for tile in background:
        window.blit(bg_image, tile)

    pygame.display.update()    

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Sky.jpg")

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    draw(window, background, bg_image)            
    
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)
    