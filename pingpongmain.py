import pygame
from pingpongrunnerhelper import pingponghelprun
from playagainstyourself import playagainstyour_self

pygame.init()

screen_width = 1150
screen_height = 900

screens = pygame.display.set_mode((screen_width, screen_height))
title = pygame.display.set_caption("Ping Pong")

bg_color = (255,255,255)
bg_image = pygame.transform.scale(pygame.image.load("firsttext.png"), (screen_width, screen_height))
info_text = pygame.font.Font(None, 30)







game_run = True

while game_run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game_run = False

    screens.fill(bg_color)


    screens.blit(bg_image, (0,0))
    

    keys = pygame.key.get_pressed()

    if keys[pygame.K_1]:
        pingponghelprun()
    if keys[pygame.K_2]:
        playagainstyour_self()






    if keys[pygame.K_ESCAPE]:
         pygame.quit()
         
         

    pygame.display.update()
    pygame.time.Clock().tick(60)









