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
    x = 800
    y = 600
elif resoultion == 2:
    x = 1920
    y = 1080
else: print("This resoultion isn't available")  


difficulty = int(input("Please choose a difficulty. Enter 1 for Normal or 2 for Encore"))

if difficulty == 1:
    pygame.display.set_caption('Normal')
else:    
    pygame.display.set_caption('Encore')

window = pygame.display.set_mode((x,y))    

def main(window):
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
    
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)
    