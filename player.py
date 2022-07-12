import pygame
from projectile import Projectile
from animation import AnimateSprite


class Player(AnimateSprite):

    def __init__(self, game):
        super().__init__("player")
        self.health = 200
        self.max_health = 200
        self.attack = 10
        self.velocity = 2
        # self.image = pygame.image.load('PygameAssets-main/monster.png')
        # self.image = pygame.transform.scale(self.image, (100, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400
        self.all_projectiles = pygame.sprite.Group()
        self.game = game

    def move_left(self):
        self.rect.x -= self.velocity

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monster):
            self.rect.x += self.velocity

    def threw_projectile(self):
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)
        self.start_animation()
        self.game.sound_manager.play('tir')

    def update_animation(self):
        self.animate(False)

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (96, 96, 96), [self.rect.x, self.rect.y - 10, self.max_health, 5])
        pygame.draw.rect(surface, (0, 255, 0), [self.rect.x, self.rect.y - 10, self.health, 5])

    def damage(self, amount):
        if self.health >= 0:
            self.health -= amount
        else:
            self.game.game_over()