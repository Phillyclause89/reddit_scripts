import pygame
import random
#initialization
pygame.init()

window = pygame.display.set_mode((1280, 800)) #creates window
pygame.display.set_caption('Sailing Too The Seven Moons') #gives name

player = pygame.image.load("PlayerShip.png") #player image
bg = pygame.image.load("SpaceBG.png") #background image

class play_char(object):
    def __init__(self, x, y, width, height, left, right):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.left = False
        self.right = False
        self.movingCount = 0
        self.be_like_that = 5

    def draw(self, window):

        if self.movingCount + 1 >= 30:
            self.movingCount = 0

        if self.left:
            window.blit(player[self.movingCount//3], (self.x, self.y))
            self.movingCount += 1
        elif self.right:
            window.blit(player[self.movingCount//3], (self.x, self.y))
            self.movingCount += 1
        else:
            window.blit(player, (self.x, self.y))
            self.movingCount = 0

class projectile(object):
    def __init__(self, y, color):
        self.y = y
        self.color = color
        self.velocity = 8

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y), 0)

clock = pygame.time.Clock() #bruh
char = play_char(300, 410, 64, 64, False, False)

def redrawGameWindow():
    window.blit(bg, (0,0))
    char.draw(window)
    for lazer in lazers:
        lazers.draw(window)

    pygame.display.update()

run = True
lazers = []
#mainloop
while run:

    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for lazer in lazers:
        if lazer.y < 800 and lazer.y > 0:
            lazer.y += lazer.vel
        else:
            lazers.pop(lazers.index(lazers))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if len(lazers) < 4+1:
            lazers.append(projectile(round(char.x + char.width //2), round(char.y + char.height//2), 6, (0,0,0)))

    #x axis/left and right, they're working fine so far
    if keys[pygame.K_d] and char.x < 1280 - char.be_like_that - char.width:
        char.left = True
        char.right = False
        char.x += char.be_like_that
    if keys[pygame.K_a] and char.x  > char.be_like_that:
        left = False
        right = True
        char.x -= char.be_like_that
    if keys[pygame.K_w] and char.y > char.be_like_that:
        left = False
        right = False
        char.y -= char.be_like_that

    if keys[pygame.K_s] and char.y < 700 - char.width - char.be_like_that:
        left = False
        right = False
        char.y += char.be_like_that

    redrawGameWindow()

pygame.quit()