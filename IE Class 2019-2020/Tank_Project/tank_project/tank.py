import pygame
pygame.init()

GREEN = (23, 165, 23)

class tank(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)
        self.image.set_colorkey(GREEN)
        pygame.draw.rect(self.image, color, [75, 75, width, height])
        self.rect = self.image.get_rect()

    def moveRight(self, pixels, wall):
        col = pygame.sprite.collide_rect(self, wall)
        if col == True:
            self.rect.x -= pixels
        else:
            self.rect.x += pixels

    def movLeft(self, pixels, wall):
        col = pygame.sprite.collide_rect(self, wall)
        if col == True:
            self.rect.x += pixels
        else:
            self.rect.x -= pixels

    def moveUp(self, pixels):
        self.rect.y -= pixels

    def moveDown(self, pixels):
        self.rect.y += pixels

    def collision(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.rect.y -= self.rect.y*2
            self.rect.x -= self.rect.x*2