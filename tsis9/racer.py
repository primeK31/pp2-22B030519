import random

import pygame

pygame.init()
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLOCK_SIZE = 40
WHITE = (255, 255, 255)
SCORE = 0
clock = pygame.time.Clock()
background = pygame.image.load('./materials/AnimatedStreet.png')
score_font = pygame.font.SysFont("Verdana", 30)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 10
        self.image = pygame.image.load('./materials/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(self.rect.width, WIDTH - self.rect.width),
            0,
        )

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        global SCORE
        self.rect.move_ip(0, self.speed)
        if self.rect.y > HEIGHT:
            SCORE += 1
            self.rect.center = (
                random.randint(self.rect.width, WIDTH - self.rect.width),
                0,
            )


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./materials/coin.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, WIDTH - 30), HEIGHT - 60)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.center = (random.randint(30, WIDTH - 30), HEIGHT - 60)

class jCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./materials/jew_coins.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, WIDTH - 30), HEIGHT - 60)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.center = (random.randint(30, WIDTH - 30), random.randint(30, HEIGHT - 30))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 5
        self.image = pygame.image.load('./materials/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.x - self.speed >= 0:
            self.rect.move_ip(-self.speed, 0)
        elif pressed[pygame.K_RIGHT] and self.rect.x + self.speed + self.rect.width <= WIDTH:
            self.rect.move_ip(self.speed, 0)
        elif pressed[pygame.K_UP] and self.rect.x - self.speed >= 0:
            self.rect.move_ip(0, -self.speed)
        elif pressed[pygame.K_DOWN] and self.rect.x + self.speed + self.rect.width <= HEIGHT:
            self.rect.move_ip(0, self.speed)


def main():
    running = True
    player = Player()
    enemy = Enemy()
    enemies = pygame.sprite.Group()
    enemies.add(enemy)
    cn = Coin()
    jew_coin = jCoin()
    jew_coins = pygame.sprite.Group()
    jew_coins.add(jew_coin)
    coin = pygame.sprite.Group()
    coin.add(cn)
    coins = 0

    while running:
        # SCREEN.fill(WHITE)
        SCREEN.blit(background, (0, 0))
        score = score_font.render(f" Your score: {SCORE}", True, (0, 0, 0))
        coins_text = score_font.render(f"Your coins: {coins}", True, (0, 0, 0))
        SCREEN.blit(score, (0, 0))
        SCREEN.blit(coins_text, (0, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update()
        enemy.update()

        player.draw(SCREEN)
        enemy.draw(SCREEN)
        coin.draw(SCREEN)
        jew_coins.draw(SCREEN)

        if pygame.sprite.spritecollideany(player, enemies):
            running = False
        if pygame.sprite.spritecollideany(player, coin):
            coins += 1
            if coins % 5 == 0:
                enemy.speed += 1
            print(enemy.speed)
            coin.update()
        if pygame.sprite.spritecollideany(player, jew_coins):
            coins += 5
            print(enemy.speed)
            jew_coins.update()

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
