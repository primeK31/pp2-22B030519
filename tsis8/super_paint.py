import pygame
pygame.init()

screen = pygame.display.set_mode((900, 700))


def round_line(canvas, color, start, end, radius=1) :
    x_axis = end[0] - start[0]
    y_axis = end[1] - start[1]
    dist = max(abs(x_axis), abs(y_axis))
    for i in range(dist):
        x = int(start[0] + float(i) / dist * x_axis)
        y = int(start[1] + float(i) / dist * y_axis)
        pygame.draw.circle(canvas, color, (x, y), radius)


def draw_rect(ch_color):
    pos = pygame.mouse.get_pos()
    rect_size = (50, 50)
    rect_pos = (pos[0] - rect_size[0] / 2, pos[1] - rect_size[1] / 2)
    pygame.draw.rect(screen, ch_color, (rect_pos, rect_size))


def draw_circle(ch_color):
    pos = pygame.mouse.get_pos()
    radius = 25
    pygame.draw.circle(screen, ch_color, pos, radius)


def main():
    running = True
    draw_on = False
    last_pos = (0, 0)
    radius = 5
    ch_color = (255, 255, 255)
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN:
                if e.key == ord("b"):
                    ch_color = (0, 0, 255)
                if e.key == ord("y"):
                    ch_color = (255, 255, 0)
                if e.key == ord("g"):
                    ch_color = (0, 255, 0)
                if e.key == ord("w"):
                    ch_color = (255, 255, 255)
                if e.key == ord("r"):
                    draw_rect(ch_color)
                if e.key == ord("c"):
                    draw_circle(ch_color)
                if e.key == ord("e"):
                    ch_color = (0, 0, 0)

            if e.type == pygame.MOUSEBUTTONDOWN:
                color = ch_color
                pygame.draw.circle(screen, color, e.pos, radius)
                draw_on = True
            if e.type == pygame.MOUSEBUTTONUP:
                draw_on = False
            if e.type == pygame.MOUSEMOTION:
                if draw_on:
                    pygame.draw.circle(screen, color, e.pos, radius)
                    round_line(screen, color, e.pos, last_pos, radius)
                last_pos = e.pos
        pygame.display.flip()


if __name__ == '__main__':
    main()
