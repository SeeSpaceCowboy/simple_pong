import pygame                   # WHAT THE HELL I'M DOING HERE?!

class block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((38, 38))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (240, 160)

    def update(self):
        self.speedx = 10
        self.speedy = 10

        if self.rect.x < 610:
            self.rect.x += self.speedx
        if self.rect.y < 440 and self.rect.y > 40:
            self.rect.y += self.speedy
            print(self.rect.y)
        elif self.rect.y >= 440 or self.rect.y <= 0:
            self.speedy = self.speedy * -1
            self.rect.y += self.speedy

class player(pygame.sprite.Sprite):
    is_first = True
    speedy = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 60))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (10, 0)

    def update(self):
        self.speedy = 0
        state = pygame.key.get_pressed()

        if (state[pygame.K_w] and self.is_first) or (state[pygame.K_i] and not self.is_first):
            self.speedy = -10
        elif (state[pygame.K_s] and self.is_first) or (state[pygame.K_k] and not self.is_first):
            self.speedy = 10

        if self.rect.y <= 420 and self.rect.y >= 0:
            self.rect.y += self.speedy
        else:
            if self.rect.y // 420 == 1:
                self.rect.y = 420
            else:
                self.rect.y = 0
