import pygame
import os

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# load player gifs (from assests) FUT make our own charecter??
player_walk_right = pygame.image.load(os.path.join(
    "assets", "char free", "char_walk_right.gif")).convert_alpha()
player_walk_left = pygame.image.load(os.path.join(
    "assets", "char free", "char_walk_left.gif")).convert_alpha()

player_rect = player_walk_right.get_rect()
player_rect.topleft = (300, 250)
current_image = player_walk_right

clock = pygame.time.Clock()

run = True

while run:
    screen.fill((0, 0, 0))

    # Draw player sprite
    screen.blit(current_image, player_rect)

    # Movement controls
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        current_image = player_walk_left
        player_rect.move_ip(-1, 0)
    elif key[pygame.K_d]:
        current_image = player_walk_right
        player_rect.move_ip(1, 0)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(10)  # Adjust the frame rate as needed

pygame.quit()
