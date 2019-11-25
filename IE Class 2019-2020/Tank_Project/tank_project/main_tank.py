import pygame
from tank import tank
pygame.init()


class Wall(pygame.sprite.Sprite):
    def __init__(self, color, sx, sy, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(DBROWN)
        self.image.set_colorkey(DBROWN)
        pygame.draw.rect(screen, color, [sx, sy, width, height], 0)
        self.rect = self.image.get_rect()

BLACK = (0, 0, 0)
RED = (255, 5, 5)
GREEN = (23, 165, 23)
GRAY = (232, 232, 232)
LBROWN = (222, 184, 135)
DBROWN = (165, 130, 85)

screenwidth = 1280
screenheight = 650
size = (screenwidth, screenheight)
screen = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption("Tank Game")

all_sprites_list = pygame.sprite.Group()

player1Tank = tank(RED, 100, 100)
player1Tank.rect.x = 75
player1Tank.rect.y = 75

all_sprites_list.add(player1Tank)

playing = True
clock = pygame.time.Clock()

def checkcol(sprite1, sprite2):
    col = pygame.sprite.collide_rect(sprite1,sprite2)
    if col == True:
        sprite1.rect.x += -10
    else:
        sprite1.rect.x += 10

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                playing = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        checkcol(player1Tank, LeftWall)
    if keys[pygame.K_RIGHT]:
        player1Tank.moveRight(10, RWall)
    if keys[pygame.K_UP]:
        player1Tank.moveUp(10)
    if keys[pygame.K_DOWN]:
        player1Tank.moveDown(10)

    all_sprites_list.update()

    screen.fill(LBROWN)

    walls = pygame.sprite.Group()
    LeftWall = Wall(DBROWN, 0, 0, 30, screenheight)
    walls.add(LeftWall)
    RWall = Wall(DBROWN, screenwidth - 30, 0, 30, screenheight)
    walls.add(RWall)
    TopWall = Wall(DBROWN, 0, 0, screenwidth, 30)
    walls.add(TopWall)
    BottomWall = Wall(DBROWN, 0, screenheight - 30, screenwidth, 30)
    walls.add(BottomWall)
    all_sprites_list.draw(screen)
    all_sprites_list.add(LeftWall, RWall, TopWall, BottomWall)




    pygame.display.flip()
    clock.tick(60)

pygame.quit()