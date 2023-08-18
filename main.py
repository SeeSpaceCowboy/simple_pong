import pygame
import classes

run = True
speed = 60

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Pong")
pygame.display.set_icon(pygame.image.load('icon.png'))

clock = pygame.time.Clock()
sprites = pygame.sprite.Group()
game_block = classes.block()

player1 = classes.player()                                      # Создание основных объектов
player2 = classes.player()
player2.rect.center = (630, 0)
player2.is_first = False
sprites.add(player1, player2, game_block)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_i:
                print('up')
            if event.key == pygame.K_s or event.key == pygame.K_k:
                print('down')

    sprites.update()
    screen.fill((0, 0, 0))
    sprites.draw(screen)
    pygame.display.flip()

    clock.tick(speed)

pygame.quit()
