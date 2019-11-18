import pygame
import linalg
import numpy as np


pygame.init()
bg = pygame.image.load('ground.png')


class Dino():
    walk = [pygame.image.load('Game/R1.png'), pygame.image.load('Game/R2.png'), pygame.image.load('Game/R3.png'),
            pygame.image.load('Game/R4.png'), pygame.image.load('Game/R5.png'), pygame.image.load('Game/R6.png'),
            pygame.image.load('Game/R7.png'), pygame.image.load('Game/R8.png'), pygame.image.load('Game/R9.png')]

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.jump = False
        self.jumpCount = 10
        self.side = 0
        self.hitbox = self.width - 33, self.height - 10

    def draw(self, gameWin):
        if not self.jump:
            gameWin.blit(self.walk[self.side//2], (self.x, self.y))
            self.side += 1
            if self.side + 1 >= 18:
                self.side = 0
        else:
            gameWin.blit(self.walk[self.side//2], (self.x, self.y))
        s = pygame.Surface((self.hitbox))
        s.set_alpha(128)
        s.fill((0,0,255))
        gameWin.blit(s, (self.x + 15, self.y + 10))


class Obstacle():
    raw_cacti = pygame.image.load('cacti-big.png')
    cacti = pygame.transform.scale(raw_cacti, (40,64))

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.hitbox = self.width-5, self.height

    def draw(self, gameWin):
        gameWin.blit(self.cacti, (self.x, self.y))
        self.move()
        s = pygame.Surface((self.hitbox))
        s.set_alpha(128)
        s.fill((0, 0, 255))
        gameWin.blit(s, (self.x + 5, self.y))

    def move(self):
        if self.x <= 0:  # obstacle
            self.x = 800
        else:
            self.x -= self.vel

def updateGameWindow():
    gameWin.fill((255,255,255))
    gameWin.blit(bg, (bg_x, 500-20))
    char.draw(gameWin)
    ob.draw(gameWin)

    pygame.display.update()


win_width = 800
win_height = 500
bg_x = 0
gameWin = pygame.display.set_mode((win_width, win_height))
char = Dino(win_width - 700, win_height - 70,64,64)
clock = pygame.time.Clock()
ob = Obstacle(win_width - 64, win_height - 64,52,101)


# Game Loop
endGame = False
while not endGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            endGame = True

    key = pygame.key.get_pressed() # Value order unknown

    if bg_x > -300: # background. continuous through 2 objects
        bg_x -= 5
    else:
        bg_x = 0

    if not char.jump: # jump. need limit consecutive jumps
        if key[pygame.K_SPACE]:
            char.jump = True
    else:
        if char.jumpCount >= -10:
            neg = 1
            if char.jumpCount < 0:
                neg = -1
            char.y -= (char.jumpCount ** 2) * 0.3 * neg
            char.jumpCount -= 1
        else:
            char.jump = False
            char.jumpCount = 10

    if key[pygame.K_UP]:
        pass

    elif key[pygame.K_UP]:
        pass

    clock.tick(40)
    updateGameWindow() # continuously update game window

pygame.quit()
