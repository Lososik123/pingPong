import pygame
import random

# Инициализируем PyGame
pygame.init()

# Параметры окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Основные цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Настраиваем экран
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ping-Pong')

# Фоновые настройки
background_color = (kartinka.jpg)

# Глобальные игровые объекты
clock = pygame.time.Clock()

# Класс ракеты
class Paddle(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.Surface([10, 100])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.speed = 10

    def update(self, direction):
        if direction == 'up' and self.rect.top > 0:
            self.rect.y -= self.speed
        elif direction == 'down' and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

# Класс мячика
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.reset_position()
        self.velocity = [random.choice([-5, 5]), random.randint(-5, 5)]

    def reset_position(self):
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.velocity = [random.choice([-5, 5]), random.randint(-5, 5)]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # Проверка столкновения с верхним и нижним краями
        if self.rect.y <= 0 or self.rect.y >= SCREEN_HEIGHT - 10:
            self.velocity[1] = -self.velocity[1]

        # Проверяем выход мяча за пределы экрана
        if self.rect.x < 0 or self.rect.x > SCREEN_WIDTH:
            self.reset_position()

# Создание спрайтов
player_1 = Paddle(20, SCREEN_HEIGHT / 2 - 50)
player_2 = Paddle(SCREEN_WIDTH - 30, SCREEN_HEIGHT / 2 - 50)
ball = Ball()

# Добавляем спрайты в группу
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player_1, player_2, ball)

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление первой ракеткой (игрок №1)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:  
        player_1.update('up')  # движение вверх
    if keys[pygame.K_s]:  
        player_1.update('down')  # движение вниз

    # Управление второй ракеткой (игрок №2)
    if keys[pygame.K_UP]:  
        player_2.update('up')  # движение вверх
    if keys[pygame.K_DOWN]:  
        player_2.update('down')  # движение вниз

    # Обновляем позицию мяча
    ball.update()

    # Проверка столкновений между мячом и ракетками
    collision_with_player1 = pygame.sprite.collide_rect(ball, player_1)
    collision_with_player2 = pygame.sprite.collide_rect(ball, player_2)

    if collision_with_player1 or collision_with_player2:
        ball.velocity[0] = -ball.velocity[0]

    # Очистка экрана
    screen.fill(background_color)

    # Рисование всех объектов
    all_sprites_list.draw(screen)

    # Обновляем экран
    pygame.display.flip()

    # Ограничение FPS
    clock.tick(FPS)

# Завершаем игру
pygame.quit()
