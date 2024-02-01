import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('SSR')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('img/Ult_pygame/Sky.jpg').convert()
ground_surface = pygame.image.load('img/Ult_pygame/Ground.jpg').convert()
text_surface = test_font.render('Sunset Runner', False, 'Blue').convert()

snail_surface = pygame.image.load('img/Ult_pygame/snail/snail1.png').convert_alpha()
snail_x_pos = 600


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(ground_surface,(0,0))
    screen.blit(sky_surface,(0,-35))
    screen.blit(text_surface,(275,50))
    snail_x_pos += -2.5
    if snail_x_pos < -100: snail_x_pos = 800
    screen.blit(snail_surface,(snail_x_pos,320))

    pygame.display.update()
    clock.tick(60)