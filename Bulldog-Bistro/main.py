import pygame
import os
import random


f = open("/dev/null", "w")
os.dup2(f.fileno(), 2)
f.close()

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Bulldog Bistro')

character_img = pygame.image.load(os.path.join('rival.png'))
character_img = pygame.transform.scale(character_img, (128, 128))

background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (1000, 800))

clock = pygame.time.Clock()

MOVEMENT_SPEED = 5


class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = character_img
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 215, 0))  # Yellow color for coin
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)


all_sprites = pygame.sprite.Group()
coins = pygame.sprite.Group()
character = Character()
all_sprites.add(character)

score = 0


def spawn_coin():
    coin = Coin()
    coins.add(coin)
    all_sprites.add(coin)


for _ in range(5):
    spawn_coin()

run = True

while run:
    game_display.fill((0, 0, 0))
    game_display.blit(background, (0, 0))

    key = pygame.key.get_pressed()
    if key[pygame.K_a] and character.rect.left > 0:
        character.rect.x -= MOVEMENT_SPEED
    if key[pygame.K_d] and character.rect.right < SCREEN_WIDTH:
        character.rect.x += MOVEMENT_SPEED
    if key[pygame.K_w] and character.rect.top > 0:
        character.rect.y -= MOVEMENT_SPEED
    if key[pygame.K_s] and character.rect.bottom < SCREEN_HEIGHT:
        character.rect.y += MOVEMENT_SPEED

    all_sprites.draw(game_display)

    collisions = pygame.sprite.spritecollide(character, coins, True)
    if collisions:
        score += len(collisions)
        for _ in range(len(collisions)):
            spawn_coin()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    font = pygame.font.SysFont(None, 36)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    game_display.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
