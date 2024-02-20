import pygame
from sys import exit
# Good work, get it finished please. 

def display_score():
    current_time = int(pygame.time.get_ticks() / 500) - start_time
    score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,70))
    screen.blit(score_surf,score_rect)
    print(current_time)

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('SSR')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True
start_time = 0

sky_surface = pygame.image.load('img/Ult_pygame/Sky.jpg').convert()
ground_surface = pygame.image.load('img/Ult_pygame/Ground.jpg').convert()

title_surface = test_font.render('Sunset Runner', False, (20, 219, 169)).convert()
title_rectangle = title_surface.get_rect(center = (400,30))

player_surface = pygame.image.load('img/Ult_pygame/Player/player_walk_1.png')
player_rectangle = player_surface.get_rect(midbottom = (80,355))
player_gravity = 0

snail_surface = pygame.image.load('img/Ult_pygame/snail/snail1.png').convert_alpha()
snail_x_rectangle = snail_surface.get_rect(bottomright = (700,355))

#doubleJump = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if game_active:        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if  player_rectangle.collidepoint(event.pos) and player_rectangle.bottom >= 320:
                player_gravity = -19.5

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rectangle.bottom >= 320:
                player_gravity = -19.5    
                #if player_rectangle.bottom >= 250 and int(doubleJump): 
                #    player_gravity = -13.9,
    else:
        if game_active == False:
            game_active = True
            snail_x_rectangle.left = 800
            print("restart")
            start_time = int(pygame.time.get_ticks() / 500)
                    
    if game_active: 
       screen.blit(ground_surface,(0,0))
       screen.blit(sky_surface,(0,-35))
       pygame.draw.rect(screen,'pink',title_rectangle)
       pygame.draw.rect(screen,(214, 13, 90),title_rectangle,1)
       pygame.draw.circle(screen,'gold',pygame.mouse.get_pos(),10)
       screen.blit(title_surface,title_rectangle)
       display_score()

       snail_x_rectangle.x -= 5.5
       if snail_x_rectangle.right <=0: snail_x_rectangle.left = 800

       screen.blit(player_surface,player_rectangle)
    
    # Player
       player_gravity += 1
       player_rectangle.y += player_gravity
       if player_rectangle.bottom >= 355: player_rectangle.bottom = 355
       screen.blit(snail_surface,snail_x_rectangle)

    # collision
    #if snail_x_rectangle.colliderect(player_rectangle):
    #    pygame.quit()
    #    exit()
       if snail_x_rectangle.colliderect(player_rectangle):
            game_active = False
    else:
        screen.fill('yellow')

    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_SPACE]:
    #    print('jump')

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