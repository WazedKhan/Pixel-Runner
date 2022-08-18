import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Pixel Runner')
clock = pygame.time.Clock()

test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
test_surface = test_font.render('Start', False, 'Black')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (900, 300))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_react = player_surface.get_rect(midbottom = (80, 300))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(test_surface, (350, 50))

    snail_rect.right -= 4
    if snail_rect.right <= -100: snail_rect.right = 900
    screen.blit(snail_surface, snail_rect)

    screen.blit(player_surface, player_react)
    player_react.left += 1

    if player_react.colliderect(snail_rect):
        print('collision')

    pygame.display.update()
    clock.tick(60)
