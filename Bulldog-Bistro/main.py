import pygame
import os
import random
import sys

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
    def __init__(self, table_positions):
        super().__init__()
        self.image = pygame.image.load('burger.png')  # Load burger image
        self.image = pygame.transform.scale(
            self.image, (32, 32))  # Resize if necessary

        self.rect = self.image.get_rect()
        # Randomly choose a table position
        self.rect.topleft = random.choice(table_positions)


all_sprites = pygame.sprite.Group()
coins = pygame.sprite.Group()
character = Character()
all_sprites.add(character)

og_plate_positions = ((97, 192),
                      (158, 192),
                      (312, 173),
                      (355, 173),
                      (283, 309),
                      (338, 292),
                      (388, 296),
                      (410, 313))  # coordniates of the plates

x_scale = background.get_width() / SCREEN_WIDTH
y_scale = background.get_height() / SCREEN_HEIGHT

# Scale and update table positions
plate_positions = [(int(x * x_scale), int(y * y_scale))
                   for x, y in og_plate_positions]


def spawn_coin():
    coin = Coin(plate_positions)
    all_sprites.add(coin)
    coins.add(coin)


def welcome_screen():
    game_display.fill((0, 0, 0))

    font = pygame.font.SysFont(None, 50)
    welcome_text = font.render(
        "Welcome to Bulldog Bistro!", True, (255, 255, 255))
    start_text = font.render("Press S to Start", True, (255, 255, 255))
    exit_text = font.render("Press E to Exit", True, (255, 255, 255))
    game_display.blit(welcome_text, (SCREEN_WIDTH // 2 -
                      welcome_text.get_width() // 2, 200))
    game_display.blit(start_text, (SCREEN_WIDTH // 2 -
                      start_text.get_width() // 2, 300))
    game_display.blit(exit_text, (SCREEN_WIDTH // 2 -
                      exit_text.get_width() // 2, 400))
    pygame.display.update()


def end_screen(score):
    game_display.fill((0, 0, 0))
    font = pygame.font.SysFont(None, 50)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    play_again_text = font.render(
        "Press S to Play Again", True, (255, 255, 255))
    exit_text = font.render("Press E to Exit", True, (255, 255, 255))
    game_display.blit(score_text, (SCREEN_WIDTH // 2 -
                      score_text.get_width() // 2, 200))
    game_display.blit(play_again_text, (SCREEN_WIDTH // 2 -
                      play_again_text.get_width() // 2, 300))
    game_display.blit(exit_text, (SCREEN_WIDTH // 2 -
                      exit_text.get_width() // 2, 400))
    pygame.display.update()


def game_loop():
    score = 0
    game_over = False
    timer = 30

    for _ in range(5):
        spawn_coin()

    while not game_over:
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

        # Check for collisions between character and coins
        collisions = pygame.sprite.spritecollide(character, coins, True)
        if collisions:
            score += len(collisions)
            for _ in range(len(collisions)):
                spawn_coin()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        font = pygame.font.SysFont(None, 36)
        text = font.render(f"Score: {str(score)}", True, (255, 255, 255))
        game_display.blit(text, (10, 10))

        # Update timer
        timer -= 1 / 60  # Decrement timer by 1/60th of a second
        if timer <= 0:
            game_over = True

        timer_text = font.render(f"Time: {int(timer)}", True, (255, 255, 255))
        game_display.blit(timer_text, (10, 50))

        pygame.display.update()

        clock.tick(60)

    end_screen(score)


def main():
    welcome_screen()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_s:
                    game_loop()
                elif event.key == pygame.K_e:
                    pygame.quit()
                    sys.exit()


if __name__ == "__main__":
    main()
