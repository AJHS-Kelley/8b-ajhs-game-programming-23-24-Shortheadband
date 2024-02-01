import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

sky_surface = pygame.image.load('img/Ult_pygame/Sky.jpg')
ground_surface = pygame.image.load('img/Ult_pygame/Ground.jpg')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(ground_surface,(0,0))
    screen.blit(sky_surface,(0,0))

    pygame.display.update()
    clock.tick(60)