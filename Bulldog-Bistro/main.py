import pygame
import os

f = open("/dev/null", "w")
os.dup2(f.fileno(), 2)
f.close()

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Bulldog Bistro')

character = pygame.image.load(os.path.join('rival.png'))
character = pygame.transform.scale(character, (128, 128))

character_width, character_height = character.get_size()  # Get character size

character_x = 370
character_y = 480

background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (1000, 800))

clock = pygame.time.Clock()

MOVEMENT_SPEED = 5

run = True

while run:
    game_display.fill((0, 0, 0))

    game_display.blit(background, (0, 0))
    game_display.blit(character, (character_x, character_y))

    key = pygame.key.get_pressed()
    if key[pygame.K_a] and character_x > 0:  # Check left boundary
        character_x -= MOVEMENT_SPEED
    if key[pygame.K_d] and character_x < SCREEN_WIDTH - character_width:  # Check right boundary
        character_x += MOVEMENT_SPEED
    if key[pygame.K_w] and character_y > 0:  # Check top boundary
        character_y -= MOVEMENT_SPEED
    if key[pygame.K_s] and character_y < SCREEN_HEIGHT - character_height:  # Check bottom boundary
        character_y += MOVEMENT_SPEED

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
