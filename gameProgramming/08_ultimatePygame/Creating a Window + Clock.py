import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('SSR')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('img/Ult_pygame/Sky.jpg')
ground_surface = pygame.image.load('img/Ult_pygame/Ground.jpg')
text_surface = test_font.render('Sunset Runner', False, 'Blue')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(ground_surface,(0,0))
    screen.blit(sky_surface,(0,-25))
    screen.blit(text_surface,(275,50))

    pygame.display.update()
    clock.tick(60)