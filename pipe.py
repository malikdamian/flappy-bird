import pygame


class Pipe(pygame.sprite.Sprite):
    def __init__(self, pos, width, height, flip) -> None:
        super().__init__()
        self.width = width
        img_path = "resource/terrain/pipe.png"
        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=pos)
        if flip:
            flipped_image = pygame.transform.flip(
                surface=self.image, flip_x=False, flip_y=True
            )
            self.image = flipped_image

    def update(self, x_shift) -> None:
        """
        Shifts the object's position by `x_shift` and removes it if it goes off the
        left side of the screen.

        :param x_shift: The `x_shift` parameter in the `update` method represents the amount by which the
        `self.rect.x` attribute will be shifted horizontally. This parameter is used to update the position
        of the object along the x-axis
        """
        self.rect.x += x_shift
        if self.rect.right < (-self.width):
            self.kill()
