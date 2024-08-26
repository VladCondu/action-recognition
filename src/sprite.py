import pygame.sprite
from PIL import Image, ImageSequence


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, x, bottom, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=(x, bottom))
        self.image_index = 0

    def update(self):
        self.image_index += 1
        if self.image_index >= len(self.images):
            self.image_index = 0
        self.image = self.images[self.image_index]

    @staticmethod
    def loadGIF(filename, scale=1):
        pil_image = Image.open(filename)
        frames = []
        for frame in ImageSequence.Iterator(pil_image):
            frame = frame.convert('RGBA')
            w, h = frame.size
            pygame_image = pygame.image.fromstring(
                frame.tobytes(), frame.size, frame.mode).convert()
            pygame_image = pygame.transform.scale(pygame_image, (scale * w, scale * h))
            frames.append(pygame_image)
        return frames
