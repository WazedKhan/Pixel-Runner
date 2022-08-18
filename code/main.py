import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Pixel Runner')
clock = pygame.time.Clock()

test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
test_surface = test_font.render('Start', False, 'Black')
snail_surface = pygame.image.load('graphics/snail/snail1.png')

snail_x = 800
snail_y = 280


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(test_surface, (350, 50))

    snail_x -= 2
    if snail_x <= -72:
        snail_x = 760

    screen.blit(snail_surface, (snail_x, snail_y))

    pygame.display.update()
    clock.tick(60)
