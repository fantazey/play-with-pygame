import pygame
import sys
import random
import pygame.locals as GAME_LOCALS
import pygame.event as GAME_EVENT
import pygame.time as GAME_TIME

pygame.init()

title_image = pygame.image.load("assets/file6/title.png")
game_over_image = pygame.image.load("assets/file6/game_over.png")

clock = GAME_TIME.Clock()

w_height = 400
w_width = 600

surface = pygame.display.set_mode((w_width, w_height))
pygame.display.set_caption("Drop!")

left_down = False
right_down = False
game_started = False
game_ended = False
game_platforms = []
platform_speed = 3
platform_delay = 2000
last_platform = 0
player_speed = 5
platforms_dropped_through = -1
dropping = False

game_begin_at = 0
timer = 0

check_pixel_color = (0, 0, 0, 255)

player = {
    "x": int(w_width / 2),
    "y": 0,
    "h": 25,
    "w": 10,
    "vy": 5
}


def draw_player():
    pygame.draw.rect(
        surface,
        (255, 0, 0),
        (player["x"], player["y"], player["w"], player["h"])
    )


def move_player():
    global platforms_dropped_through, dropping, player

    left_on_platform = surface.get_at((player["x"], player["y"] + player["h"])) != check_pixel_color
    right_on_platform = surface.get_at((player["x"] + player["w"], player["y"] + player["h"])) != check_pixel_color

    can_fall = player["y"] + player["h"] + player["vy"] < w_height

    if not left_on_platform and not right_on_platform and can_fall:
        player["y"] += player["vy"]

        if not dropping:
            dropping = True
            platforms_dropped_through += 1

    else:
        platform_top_found = False
        y_offset = 0
        dropping = False

        while not platform_top_found:
            if surface.get_at((player["x"], player["y"] + player["h"] - y_offset)) == check_pixel_color:
                player["y"] -= y_offset
                platform_top_found = True
            elif (player["y"] + player["h"]) - y_offset > 0:
                y_offset += 1
            else:
                game_over()
                break

    horizontal_movement()


def horizontal_movement():
    global player
    if left_down and player["x"] > 0 and player["x"] - player_speed > 0:
        player["x"] -= player_speed

    right_border = player["x"] + player["w"]
    if right_down and right_border < w_width:
        if right_border + player_speed < w_width:
            player["x"] += player_speed
        else:
            player["x"] = w_width - player["w"] - player_speed


def create_platform():
    global last_platform, platform_delay

    platform_y = w_height
    gap = random.randint(0, w_width - 40)
    new_platform = {
        "pos": [0, platform_y],
        "gap": gap
    }
    game_platforms.append(new_platform)
    last_platform = GAME_TIME.get_ticks()

    if platform_delay > 800:
        platform_delay -= 50


def move_platforms():
    for index, platform in enumerate(game_platforms):
        platform["pos"][1] -= platform_speed

        if platform["pos"][1] < -10:
            game_platforms.pop(index)


def draw_platforms():
    for platform in game_platforms:
        pygame.draw.rect(
            surface,
            (255, 255, 255),
            (platform["pos"][0], platform["pos"][1], w_width, 10)
        )
        pygame.draw.rect(
            surface,
            (0, 0, 0),
            (platform["gap"], platform["pos"][1], 40, 10)
        )


def game_over():
    global game_started, game_ended, platform_speed
    platform_speed = 0
    game_started = False
    game_ended = True


def restart_game():
    global game_platforms, player, game_begin_at, platforms_dropped_through, platform_delay
    game_platforms = []
    player["x"] = int(w_width / 2)
    player["y"] = 0
    game_begin_at = GAME_TIME.get_ticks()
    platforms_dropped_through = -1
    platform_delay = 2000


def quit_game():
    pygame.quit()
    sys.exit()


while True:
    surface.fill((0, 0, 0))
    for event in GAME_EVENT.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_down = True
            if event.key == pygame.K_RIGHT:
                right_down = True
            if event.key == pygame.K_ESCAPE:
                quit_game()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_down = False
            if event.key == pygame.K_RIGHT:
                right_down = False

            if event.key == pygame.K_SPACE and not game_started:
                restart_game()
                game_started = True

        if event.type == GAME_LOCALS.QUIT:
            quit_game()

    if game_started:
        timer = GAME_TIME.get_ticks() - game_begin_at
        move_platforms()
        draw_platforms()
        move_player()
        draw_player()
    elif game_ended:
        surface.blit(game_over_image, (0, 0))
    else:
        surface.blit(title_image, (0, 0))

    if GAME_TIME.get_ticks() - last_platform > platform_delay:
        create_platform()

    clock.tick(90)
    pygame.display.update()
