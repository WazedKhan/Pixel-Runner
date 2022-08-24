from random import randint
import pygame
import sys

def display_score():
    time = (int(pygame.time.get_ticks()/1000) - start_time)
    score_surf = test_font.render(f'Score: {time}', False, (64,64,64))
    score_ract = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_ract)
    return time


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.right -= 5

            screen.blit(snail_surface, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.right > -10]

        return obstacle_list
    else: return []

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Pixel Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# score_surf = test_font.render('Pixel Runner', False, (64,64,64))
# score_ract = score_surf.get_rect(center = (400, 50))

# obstacles

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (900, 300))

obstacle_rect_list = []

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_react = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0

# intro screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

game_title = test_font.render('Pixel Runner', False, (64,64,64))
game_title_rect = game_title.get_rect(midtop = (400, 50))
game_start_instraction = test_font.render('Press "Space" to start the game', False, (64,64,64))
game_start_instraction_rect= game_start_instraction.get_rect(midtop = (400, 350))

score = 0

# timer
obstacle_timer = pygame.USEREVENT+1
pygame.time.set_timer(obstacle_timer, 1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_react.collidepoint(event.pos) and player_react.bottom == 300:
                    player_gravity = -22

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_react.bottom == 300:
                    player_gravity = -22
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                snail_rect.right = 900
                player_react.bottom = 300
                start_time = int(pygame.time.get_ticks()/1000)
                game_active = True

        if event.type == obstacle_timer and game_active:
            obstacle_rect_list.append(snail_surface.get_rect(midbottom = (randint(900, 1100), 300)))

    if game_active:
        # background
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()

        # obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Player
        player_gravity += 1
        player_react.bottom += player_gravity
        if player_react.bottom >= 300: player_react.bottom = 300
        screen.blit(player_surface, player_react)

        # Collision
        if player_react.colliderect(snail_rect):
            game_active = False
            screen.blit(player_stand, player_stand_rect)
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_title, game_title_rect)

        score_message = test_font.render(f'Your score: {score}', False, (64, 64, 64))
        score_message_rect = score_message.get_rect(center = (400, 340))

        if score != 0: screen.blit(score_message, score_message_rect)
        else: screen.blit(game_start_instraction, game_start_instraction_rect)



    pygame.display.update()
    clock.tick(60)
