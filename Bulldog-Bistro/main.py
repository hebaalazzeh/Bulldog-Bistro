import pygame
import os

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Bulldog Bistro')  # Fixed typo in set_caption

white_color = (255, 255, 255)

# Corrected typo: pygame.image.load
# character_image = pygame.image.load('assets/rival.png')
# os.path.dirname(os.path.abspath('rival.png'))


"""def add_character_at_location(x, y):
    game_display.blit(character_image, (x, y))"""


character_x = SCREEN_WIDTH // 2
character_y = SCREEN_HEIGHT // 2

clock = pygame.time.Clock()

run = True

while run:
    # Changed "screen" to "game_display" to match the display surface
    game_display.fill((0, 0, 0))

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
