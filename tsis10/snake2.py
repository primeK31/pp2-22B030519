import random
import pygame
import psycopg2

pygame.init()
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLOCK_SIZE = 40

clock = pygame.time.Clock()


class Button:  # если ты фигуру изволишь изменить - то унаследуй (pygame.sprite.Sprite)
    def __init__(self, x, y):
        # super().__init__() и вот это раскомментируй
        self.x = x
        self.y = y
        self.rect = pygame.draw.rect(
            SCREEN,
            (0, 0, 0),
            (self.x, self.y, 40, 40)
        )

    def draw(self):
        self.rect = pygame.draw.rect(
            SCREEN,
            WHITE,
            (self.x, self.y, 40, 40)
        )


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        self.body = [
        Point(
            x=WIDTH // BLOCK_SIZE // 2,
            y=HEIGHT // BLOCK_SIZE // 2,
        ),
            #Point(
            #    x=WIDTH // BLOCK_SIZE // 2 + 1,
            #    y=HEIGHT // BLOCK_SIZE // 2,),
        ]


    def draw(self):
        head = self.body[0]
        pygame.draw.rect(
            SCREEN, RED,
            pygame.Rect(head.x * BLOCK_SIZE,
                        head.y * BLOCK_SIZE,
                        BLOCK_SIZE, BLOCK_SIZE)
        )
        for body in self.body[1:]:
            pygame.draw.rect(
                SCREEN, BLUE,
                pygame.Rect(body.x * BLOCK_SIZE,
                            body.y * BLOCK_SIZE,
                            BLOCK_SIZE, BLOCK_SIZE)
            )


    def move(self, dx, dy):
        for idx in range(len(self.body) - 1, 0, -1):
            self.body[idx].x = self.body[idx - 1].x
            self.body[idx].y = self.body[idx - 1].y
        self.body[0].x += dx
        self.body[0].y += dy

        if self.body[0].x > WIDTH // BLOCK_SIZE:
            self.body[0].x = 0
        elif self.body[0].x < 0:
            self.body[0].x = WIDTH // BLOCK_SIZE
        elif self.body[0].y < 0:
            self.body[0].y = WIDTH // BLOCK_SIZE
        elif self.body[0].y > HEIGHT // BLOCK_SIZE:
            self.body[0].y = 0

    def check_collision(self, food):
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True

    def check_wall(self):
        for i in self.body[1:]:
            if i.x == self.body[0].x and i.y == self.body[0].y:
                return True


def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, BLACK, start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, BLACK, start_pos=(0, y), end_pos=(WIDTH, y), width=1)


class Food:
    def __init__(self, x, y):
        self.location = Point(x, y)

    def draw(self):
        pygame.draw.rect(SCREEN, GREEN,
                         pygame.Rect(
                             self.location.x * BLOCK_SIZE,
                             self.location.y * BLOCK_SIZE,
                             BLOCK_SIZE, BLOCK_SIZE,
                         ))


class SuperFood(Food):
    def draw(self):
        pygame.draw.rect(SCREEN, (155, 155, 155),
                        pygame.Rect(
                            self.location.x * BLOCK_SIZE,
                            self.location.y * BLOCK_SIZE,
                            BLOCK_SIZE, BLOCK_SIZE,
                        ))


class Wall:
    def __init__(self):
        self.body = list()
        for i in range(0, 20):
            for j in range(0, 20):
                if i == 0 or j == 0:
                    self.body.append(Point(i, j))


    def draw(self):
        for i in self.body:
            pygame.draw.rect(SCREEN, GREEN,
                         pygame.Rect(
                             i.x * BLOCK_SIZE,
                             i.y * BLOCK_SIZE,
                             BLOCK_SIZE, BLOCK_SIZE,
                         ))


def main():
    score = 0
    conn = psycopg2.connect(
        host="localhost",
        database="phonebook",
        user="postgres",
        password="pass123"
    )

    cur = conn.cursor()
    is_user = False
    is_user_save = False
    user_name = input("Enter name: ")
    query = """SELECT user_name, user_score FROM user1 INNER JOIN user2 on user1.id = user2.id;"""
    cur.execute(query)
    row = cur.fetchall()
    for i in row:
        if i[0] == user_name:
            score = i[1]
            is_user = True
    query3 = """SELECT user_name FROM user3;"""
    cur.execute(query3)
    row4 = cur.fetchall()
    for i in row4:
        if i[0] == user_name:
            is_user_save = True
    snake = Snake()
    wall = Wall()
    row3 = list()
    if is_user and is_user_save:
        query3 = """SELECT x, y, user_name FROM user3"""
        cur.execute(query3)
        row3 = cur.fetchall()
        snake.body.pop()
        for i in row3[:]:
            if user_name == i[2]:
                snake.body.append(Point(i[0], i[1]))
    running = True
    food = Food(5, 5)
    fps = 5
    level = 1
    score_font = pygame.font.SysFont("Verdana", 30)
    dx, dy = 0, 0
    isDown = False
    isLeft = False
    isRight = False
    isUp = False
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    counter = 0
    isDraw = True
    is_drawn = False
    superFood = SuperFood(1, 1)
    pause_button = Button(50, 50)
    resume_button = Button(100, 50)
    is_ready = False
    if score >= 5:
        level = 2

    while running:
        SCREEN.fill(WHITE)
        if counter >= 40 and counter <= 50 and isDraw:
            superFood.draw()
            is_drawn = True
        score_text = score_font.render(f" Your score: {score}", True, (0, 0, 0))
        level_text = score_font.render(f" Level: {level}", True, (0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                counter += 1
                if counter >= 60:
                    counter = 0
                if counter == 51:
                    superFood.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
                    superFood.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
                print(counter)
            if event.type == pygame.QUIT:
                if is_user:
                    delete_xy = """DELETE FROM user3 WHERE user_name = %s"""
                    cur.execute(delete_xy, (user_name,))
                for i in snake.body:  # INNER JOIN user1 on user1.id = user3.id
                    insert_xy = """INSERT INTO user3(x, y, user_name) 
                                    VALUES(%s, %s, %s);"""
                    cur.execute(insert_xy, (i.x, i.y, user_name,))
                running = False
            if event.type == pygame.KEYDOWN:
                is_ready = True
                if event.key == pygame.K_e:
                    is_ready = False
                    if is_user:
                        update = """ UPDATE user2
                                    SET user_score = %s FROM user1
                                    WHERE user1.id = user2.id and user1.user_name = %s"""
                        cur.execute(update, (score, user_name))
                    else:
                        add_user = """INSERT into user1 (user_name)
                                        VALUES (%s);"""
                        add_score = """INSERT INTO user2 (user_score)
                                        VALUES (%s);"""
                        cur.execute(add_user, (user_name,))
                        cur.execute(add_score, (score,))
                        is_user = True
                if event.key == pygame.K_UP and not isDown:
                    isUp = True
                    isDown = False
                    isRight = False
                    isLeft = False
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN and not isUp:
                    dx, dy = 0, 1
                    isUp = False
                    isDown = True
                    isRight = False
                    isLeft = False
                elif event.key == pygame.K_RIGHT and not isLeft:
                    dx, dy = 1, 0
                    isUp = False
                    isDown = False
                    isRight = True
                    isLeft = False
                elif event.key == pygame.K_LEFT and not isRight:
                    dx, dy = -1, 0
                    isUp = False
                    isDown = False
                    isRight = False
                    isLeft = True

        if is_ready:
            snake.move(dx, dy)
        if snake.check_wall() and is_ready:
            running = False
        if snake.check_collision(food):
            snake.body.append(Point(snake.body[-1].x, snake.body[-1].y))
            food.location.x = random.randint(1, WIDTH // BLOCK_SIZE - 1)
            food.location.y = random.randint(1, HEIGHT // BLOCK_SIZE - 1)
            if food.location in snake.body:
                food.location.x = random.randint(1, WIDTH // BLOCK_SIZE - 1)
                food.location.y = random.randint(1, HEIGHT // BLOCK_SIZE - 1)
            score += 1
            if score % 5 == 0:
                fps += 2
                level += 1
        if snake.check_collision(superFood):
            if is_drawn:
                snake.body.append(Point(snake.body[-1].x, snake.body[-1].y))
                superFood.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
                superFood.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
                isDraw = False
                is_drawn = False
                score += 6
        for i in wall.body:
            if snake.body[0].x == i.x and snake.body[0].y == i.y:
                running = False
        snake.draw()
        food.draw()
        if level > 1:
            wall.draw()
        pause_button.draw()
        resume_button.draw()
        draw_grid()
        SCREEN.blit(score_text, (0, 0))
        SCREEN.blit(level_text, (0, 50))
        pygame.display.flip()
        clock.tick(fps)
    if is_user:
        update = """ UPDATE user2
                    SET user_score = %s FROM user1
                    WHERE user1.id = user2.id and user1.user_name = %s"""
        cur.execute(update, (score, user_name))
    else:
        add_user = """INSERT into user1 (user_name)
                        VALUES (%s);"""
        add_score = """INSERT INTO user2 (user_score)
                        VALUES (%s);"""
        cur.execute(add_user, (user_name,))
        cur.execute(add_score, (score,))
    conn.commit()

    cur.close()
    conn.close()


if __name__ == '__main__':
    main()
