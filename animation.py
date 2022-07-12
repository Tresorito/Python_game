import pygame
from random import randint


class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f"PygameAssets-main/{sprite_name}.png")
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0
        self.images = animations[sprite_name]
        self.animation = False

    def start_animation(self):
        self.animation = True

    def animate(self, loop: bool):
        if self.animation:
            # passer à l'image suivante
            self.current_image += randint(0, 1)

            # vérifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                self.current_image = 0
                if loop is False:
                    self.animation = False

            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


def load_animation_sprite(sprite_name):
    images = []
    for num in range(1, 25):
        path = f"PygameAssets-main/{sprite_name}/{sprite_name}{num}.png"
        images.append(pygame.image.load(path))

    return images


animations = {'mummy': load_animation_sprite("mummy"), 'player': load_animation_sprite('player'),
              'alien': load_animation_sprite('alien')}
