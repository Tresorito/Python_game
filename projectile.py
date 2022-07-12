import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.image = pygame.image.load('PygameAssets-main/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + self.image.get_width() + 80
        self.rect.y = player.rect.y - self.image.get_width() + 120
        self.velocity = 2
        self.player = player
        self.original_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 15
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def rm(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        for monster in self.player.game.check_collision(self, self.player.game.all_monster):
            self.rm()
            monster.damage(self.player.attack)

        if self.rect.x > 1080:
            self.rm()