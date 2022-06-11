import pygame
pygame.init()

width = 800
height = 600
window = pygame.display.set_mode((width, height))
clock = time.Clock()
direction = 0

class GameSprite(sprite.Sprite):
   def __init__(self, y, x, player_image, player_x, player_y, player_speed):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (x, y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
#управление
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx - 50, self.rect.top, 75, 60, -10)
        bullets.add(bullet)

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
           self.kill()
           global bullet_shot = False
class Enemy(GameSprite):
   def update(self):
       if self.rect.x >= 50 and self.rect.x <= 450 and i == 0:
            self.rect.x += 10
       if self.rect.x >= 450:
            self.rect.y += 25
            i += 1
       if self.rect.x <= 50:
            self.rect.y += 25
            i -= 1
        if self.rect.x >= 50 and self.rect.x <= 450 and i == 1:
            self.rect.x -= 10
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx - 50, self.rect.top, 75, 60, -10)
        bullets.add(bullet)

game = True
finish = False
run = True
bullet_shot = False

while game != False:
    pygame.display.update()
    clock.tick(40)

    if ent.key = Key_Space and bullet_shot == False:
        player.fire()
        

    for e in event.get():
        if e.type == QUIT:
            run = False
 
    if not finish:
        window.blit(background,(0,0))

        Bullet.update()
        
        player.update()
        
        enemy.update()





            

