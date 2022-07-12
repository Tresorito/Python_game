import pygame
from game import Game

pygame.init()

timer = pygame.time.Clock()

game = Game()

pygame.display.set_caption('-----')
screen = pygame.display.set_mode((1000, 600))

background = pygame.image.load('PygameAssets-main/bg.jpg')
banner = pygame.image.load('PygameAssets-main/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = screen.get_width()/2 - banner.get_width()/2

button = pygame.image.load('PygameAssets-main/button.png')
button = pygame.transform.scale(button, (400, 150))
button_rect = button.get_rect()
button_rect.x = 310
button_rect.y = 360

running = True
while running:
    screen.blit(background, (0, -300))

    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(button, button_rect)
        screen.blit(banner, banner_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.threw_projectile()
                else:
                    game.start()
                    game.sound_manager.play('click')

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                game.start()
                game.sound_manager.play('click')

    timer.tick(120)
