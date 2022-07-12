import pygame
from comet import Comet


class CometFallDown:

    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 10
        self.all_comets = pygame.sprite.Group()
        self.fall_mode = False
        self.game = game

    def add_percent(self):
        self.percent += self.percent_speed/100

    def is_full(self):
        return self.percent >= 100

    def reset_bar(self):
        self.percent = 0

    def meteo_commet(self):
        for i in range(10):
            self.all_comets.add(Comet(self))

    def attempt_comet(self):
        if self.is_full() and len(self.game.all_monster) == 0:
            print("Pluie de commetes")
            self.meteo_commet()
            self.fall_mode = True

    def update_bar(self, surface):
        self.add_percent()
        pygame.draw.rect(surface, (0, 0, 0), [0, surface.get_height() - 20, surface.get_width(), 10])
        pygame.draw.rect(surface, (255, 0, 0), [0, surface.get_height() - 20, (surface.get_width()/100)*self.percent, 10
                                                ])

