import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Pixel Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surf = test_font.render('Pixel Runner', False, (64,64,64))
score_ract = score_surf.get_rect(center = (400, 50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (900, 300))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_react = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_react.collidepoint(event.pos) and player_react.bottom == 300:
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_react.bottom == 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.right = 900

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        pygame.draw.rect(screen, "#c0e8ec", score_ract)
        pygame.draw.rect(screen, '#c0e8ec', score_ract, 10)
        screen.blit(score_surf, score_ract)

        snail_rect.right -= 4
        if snail_rect.right <= -100: snail_rect.right = 900
        screen.blit(snail_surface, snail_rect)

        # Player
        player_gravity += 1
        player_react.bottom += player_gravity
        if player_react.bottom >= 300: player_react.bottom = 300
        screen.blit(player_surface, player_react)

        # Collision
        if player_react.colliderect(snail_rect):
            game_active = False

    pygame.display.update()
    clock.tick(60)
