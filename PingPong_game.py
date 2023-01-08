from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image,  player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Paddle(GameSprite):
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_length - 150:
            self.rect.y += self.speed
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_length - 150:
            self.rect.y += self.speed
        

win_height = 600
win_length = 500

BLUE = (173, 216, 230)
window = display.set_mode((win_height, win_length))
display.set_caption("Ping Pong Game")
window.fill(BLUE)

paddle1 = "ned.png"
paddle2 = "the_rock.png"
ball = "ping_pong_ball.png"

paddleLeft = Paddle(paddle1, 20, 200, 30, 150, 50)
paddleRight = Paddle(paddle2, 520, 200, 30 ,150, 50)
ball = GameSprite(ball, 330, 200, 50, 50, 50)

run = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None,35)
lose1 = font.render("NED HAS LOST", True, (180,0,0))
lose2 = font.render("THE ROCK HAS LOST", True, (180,0,0))

speed_x = 2
speed_y = 2

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if finish != True:
        window.fill(BLUE)
        paddleLeft.update_left()
        paddleRight.update_right()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(paddleLeft, ball) or sprite.collide_rect(paddleRight, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = False
            window.blit(lose1, (200,200))

        if ball.rect.x > win_height:
            finish = False
            window.blit(lose2, (200,200))



        paddleLeft.reset()
        paddleRight.reset()
        ball.reset()


    
        
    


    display.update()
    clock.tick(FPS)
