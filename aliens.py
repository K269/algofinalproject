import pygame
pygame.init()

width = 800
height = 600
window = pygame.display.set_mode((width, height))
clock = time.Clock()

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

game = True
finish = False
run = True
bullet_shot = False

while game != False:
    pygame.display.update()
    clock.tick(40)
        
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
               shot = False
            if e.key == K_A:
                pass
            if e.key == K_D:
                pass
 
    if not finish:
        window.blit(background,(0,0))

        Bullet.update()
        
        player.update()
        
        enemy.update()





            

