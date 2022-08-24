from random import randint
from re import L
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

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.right > -10]

        return obstacle_list
    else: return []

def collisions(player, obstacle):
    if obstacle:
        for obstacle_rect in obstacle:
            if player.colliderect(obstacle_rect):
                return False
    return True

def player_animation():
    # play walking animation if player is on floor
    # display jump surface if player is not not floor
    global player_surface, player_index
    if player_rect.bottom < 300:
        player_surface = player_jump
    else:
        player_index += .1
        if player_index >= len(player_walk): player_index = 0
        player_surface = player_walk[int(player_index)]

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
fly_surface = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()

obstacle_rect_list = []

# player
player_walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()

player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom = (80, 300))
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
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity = -22

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -22
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player_rect.bottom = 300
                start_time = int(pygame.time.get_ticks()/1000)
                game_active = True

        if event.type == obstacle_timer and game_active:
            if randint(0, 2):
                obstacle_rect_list.append(snail_surface.get_rect(midbottom = (randint(900, 1100), 300)))
            else:
                obstacle_rect_list.append(fly_surface.get_rect(midbottom = (randint(900, 1100), 210)))

    if game_active:
        # background
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()

        # obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Player
        player_gravity += 1
        player_rect.bottom += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        player_animation()
        screen.blit(player_surface, player_rect)

        # Collision
        game_active = collisions(player_rect, obstacle_rect_list)
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_title, game_title_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0

        score_message = test_font.render(f'Your score: {score}', False, (64, 64, 64))
        score_message_rect = score_message.get_rect(center = (400, 340))

        if score != 0: screen.blit(score_message, score_message_rect)
        else: screen.blit(game_start_instraction, game_start_instraction_rect)



    pygame.display.update()
    clock.tick(60)
