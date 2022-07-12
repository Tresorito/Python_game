import pygame
from random import randint
from animation import AnimateSprite


class Monster(AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        # self.image = pygame.image.load('PygameAssets-main/mummy.png')
        # self.image = pygame.transform.scale(self.image, (130, 160))
        self.rect = self.image.get_rect()
        self.rect.x = 950 + randint(0, 300)
        self.rect.y = 440 - offset
        self.game = game
        self.default_speed = 1
        self.velocity = 2
        self.loot_amount = 10
        # self.start_animation()

    def move(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
            self.start_animation()
        else:
            self.game.player.damage(self.attack)

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = randint(1, speed)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def update_animation(self):
        self.animate(True)

    def update_health_bar(self, surface):
        color_bar = (0, 255, 0)
        color_back_bar = (96, 96, 96)
        position_bar = [self.rect.x + 10, self.rect.y - 15, self.health, 5]
        position_back_bar = [self.rect.x + 10, self.rect.y - 15, self.max_health, 5]
        pygame.draw.rect(surface, color_back_bar, position_back_bar)
        pygame.draw.rect(surface, color_bar, position_bar)

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            self.game.add_score(self.loot_amount)
            self.rect.x = 950 + randint(0, 300)
            self.health = self.max_health
            self.velocity = randint(1, self.default_speed)

        if self.game.commet_fall.is_full():
            self.game.all_monster.remove(self)
            self.game.commet_fall.attempt_comet()


class Mummy(Monster):
    def __init__(self, game):
        super().__init__(game, 'mummy', (130, 130))
        self.set_speed(3)
        self.set_loot_amount(10)


class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, 'alien', (300, 300), 140)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.health = 250
        self.max_health = 250
        self.attack = 0.8
        self.set_speed(1)
        self.set_loot_amount(50)

