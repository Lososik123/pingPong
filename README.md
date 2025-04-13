# pingPong
from pygame import *
 
class GameSprite(sprite.Sprite): #Основной класс спрайта
    def __init__(self, player_image, player_x, player_y, player_speed, size_x=65, size_y=65):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 
 
 
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

win_width = 700
win_height = 500
 
window = display.set_mode((win_width, win_height))
display.set_caption('PingPong')
background = transform.scale(image.load('kartinka.jpg'), (win_width, win_height))
 
 
player = Player('raketka.png', 325, 400, 10)

clock = time.Clock()
FPS = 60 
game = True
finish = False
while game:
 
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish == False:
        window.blit(background, (0,0))
        player.update()
        player.reset()


    display.update()
    clock.tick(FPS)
