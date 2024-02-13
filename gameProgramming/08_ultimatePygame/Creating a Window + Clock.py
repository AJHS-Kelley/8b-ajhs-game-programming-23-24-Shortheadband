import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('SSR')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('img/Ult_pygame/Sky.jpg').convert()
ground_surface = pygame.image.load('img/Ult_pygame/Ground.jpg').convert()

score_surface = test_font.render('Sunset Runner', False, (20, 219, 169)).convert()
score_rectangle = score_surface.get_rect(center = (400,50))

player_surface = pygame.image.load('img/Ult_pygame/Player/player_walk_1.png')
player_rectangle = player_surface.get_rect(midbottom = (80,355))

snail_surface = pygame.image.load('img/Ult_pygame/snail/snail1.png').convert_alpha()
snail_x_rectangle = snail_surface.get_rect(bottomright = (700,355))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if  player_rectangle.collidepoint(event.pos): print('collsion')
        if event.type ==pygame.KEYDOWN:
            print('Key Down')

        if event.type ==pygame.KEYUP:
            print('Key Up')

    screen.blit(ground_surface,(0,0))
    screen.blit(sky_surface,(0,-35))
    pygame.draw.rect(screen,'pink',score_rectangle)
    pygame.draw.rect(screen,(214, 13, 90),score_rectangle,1)
    pygame.draw.circle(screen,'gold',pygame.mouse.get_pos(),10)
    screen.blit(score_surface,score_rectangle)

    snail_x_rectangle.x -= 3
    if snail_x_rectangle.right <=0: snail_x_rectangle.left = 800

    screen.blit(player_surface,player_rectangle)
    screen.blit(snail_surface,snail_x_rectangle)

    #keys =pygame.key.get_pressed()
    #if keys[pygame.K_SPACE]:
    #    print('jump')

    #if player_rectangle.colliderect(snail_x_rectangle):
    #    print('collision')
    
    #mouse_position = pygame.mouse.get_pos()
    #if player_rectangle.collidepoint((x,y)):
    #    print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)