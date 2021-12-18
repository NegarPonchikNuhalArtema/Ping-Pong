from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

Class rackets(GameSprite):

win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("pinpong")
back = transform.scale(image.load("zamok.jpg"), (win_width, win_height))5
window.fill(back)

clock = time.Clock()
FPS = 60
game = True

def update_l(self):
    keys = key.get_pressed()
    if keys[K_w] and self.rect.y >5:
        self.rect.y -= self.speed

def update_l(self):
    keys = key.get_pressed()
    if keys[K_s] and self.rect.y >5:
        self.rect.y -= self.speed

def update_l(self):
    keys = key.get_pressed()
    if keys[K_UP] and self.rect.y >5:
        self.rect.y -= self.speed

def update_l(self):
    keys = key.get_pressed()
    if keys[K_DOWN] and self.rect.y >5:
        self.rect.y -= self.speed

speed_x = 3
speed_y = 3

while game:
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

font1 = font.Font(None, 35)
lose1 = font1.render(
    'ИГРОК 1 ПЕРЕИГРАН', True, (180, 0, 0))

while game:
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))

    if ball.rect.y > win_height-50
        or ball.rect.y < 0:
            speed_y *= -1

    if sprite.collide_rect(racket1, ball)
        or sprite.collide_rect(racket2, ball):
            speed_x *= -1

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

display.update()
clock.tick(FPS)