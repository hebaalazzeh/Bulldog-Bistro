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
character = pygame.transform.scale(character, (50, 100))

character_x = 370
character_y = 480

background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (1000, 800))

clock = pygame.time.Clock()

run = True

while run:

    # Changed "screen" to "game_display" to match the display surface
    game_display.fill((0, 0, 0))

    game_display.blit(background, (0, 0))
    game_display.blit(character, (370, 480))
    

    # Draw character at current location
    # add_character_at_location(character_x, character_y)

    # Movement controls
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        character_x -= 1
    if key[pygame.K_d]:
        character_x += 1
    if key[pygame.K_w]:
        character_y -= 1
    if key[pygame.K_s]:
        character_y += 1

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(60)  # Adjust the frame rate as needed

pygame.quit()

