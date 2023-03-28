import pygame

pygame.init()
HEIGHT, WIDTH = 400, 400
screen = pygame.display.set_mode(size=(HEIGHT, WIDTH))
x, y = 100, 100
step = 20
running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y - 25 <= 0:
                    y = 25
                else:
                    y -= step
            if event.key == pygame.K_DOWN:
                if y + 25 >= 700:
                    y = 675
                else:
                    y += step
            if event.key == pygame.K_LEFT:
                if x - 25 <= 0:
                    x = 25
                else:
                    x -= step
            if event.key == pygame.K_RIGHT:
                if x + 25 >= 700:
                    x = 675
                else:
                    x += step

    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
    pygame.display.flip()
