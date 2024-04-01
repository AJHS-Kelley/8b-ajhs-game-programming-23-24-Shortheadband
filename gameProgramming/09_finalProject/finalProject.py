# FinalProject v0.0 by Gabriel Coffey
import sys, random, pygame

resoultion = 0 # 0 = LRes(800,600) 1 = HRes(1920,1080)

if resoultion == 0:
    x = 800
    y = 600
elif resoultion == 1:
    x = 1920
    y = 1080
else: print("This resoultion isn't available")  

pygame.init()

difficulty = int(input("Please choose a difficulty. Enter 1 for Normal or 2 for Encore"))

if difficulty == 1:
    pygame.display.set_caption('Normal')
else:    
    pygame.display.set_caption('Encore')

screen = pygame.display.set_mode((x,y))





