import pygame
from player import Player
from monster import Mummy
from monster import Alien
from comet_event import CometFallDown
from sound import SoundManager


class Game:

    def __init__(self):
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monster = pygame.sprite.Group()
        self.pressed = {}
        self.commet_fall = CometFallDown(self)
        self.score = 0
        self.font = pygame.font.Font('PygameAssets-main/SecularOne-Regular.ttf', 16)
        self.sound_manager = SoundManager()

    def spawn_monster(self, monster_class_name):
        self.all_monster.add(monster_class_name.__call__(self))

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        # self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score(self, points):
        self.score += points

    @staticmethod
    def check_collision(sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def game_over(self):
        self.all_monster = pygame.sprite.Group()
        self.commet_fall.all_comets = pygame.sprite.Group()
        self.player.all_projectiles = pygame.sprite.Group()
        self.commet_fall.reset_bar()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.score = 0
        self.sound_manager.play('game_over')

    def update(self, screen):

        score_text = self.font.render(f'Score: {self.score}', 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        screen.blit(self.player.image, self.player.rect)

        self.player.update_health_bar(screen)

        self.player.update_animation()

        self.commet_fall.update_bar(screen)

        for projectile in self.player.all_projectiles:
            projectile.move()

        for monster in self.all_monster:
            monster.move()
            monster.update_health_bar(screen)
            monster.update_animation()

        for commet in self.commet_fall.all_comets:
            commet.fall()

        self.player.all_projectiles.draw(screen)

        self.all_monster.draw(screen)

        self.commet_fall.all_comets.draw(screen)

        self.pressed = pygame.key.get_pressed()
        if self.pressed[pygame.K_RIGHT] and self.player.rect.x < 820:
            self.player.move_right()
        elif self.pressed[pygame.K_LEFT] and self.player.rect.x > -1:
            self.player.move_left()