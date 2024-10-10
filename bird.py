import pygame

from settings import import_sprite

class Bird(pygame.sprite.Sprite):
    def __init__(self, pos, size) -> None:
        # bird basic info
        super().__init__()
        self.frame_index = 0
        self.animation_delay = 3
        self.jump_move = -9
        # bird animation
        self.bird_img = import_sprite('resource/bird')
        self.image = self.bird_img[self.frame_index]
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft=pos)
        self.mask = pygame.mask.from_surface(self.image)
        # bird status
        self.direction = pygame.math.Vector2(0, 0)
        self.score = 0

    def _animate(self) -> None:
        """
        Updates the image of a sprite based on a
        list of images and handles animation logic.
        """
        sprites = self.bird_img
        sprite_index = (self.frame_index // self.animation_delay) % len(sprites)
        self.image = sprites[sprite_index]
        self.frame_index += 1
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.frame_index // self.animation_delay > len(sprites):
            self.frame_index = 0

    def _jump(self) -> None:
        """
        Updates the y direction of an object to perform a jump movement.
        """
        self.direction.y = self.jump_move

    def update(self, is_jump) -> None:
        """
        Checks if a jump action is requested and performs the jump if needed, then
        proceeds to animate.

        :param is_jump: The `is_jump` parameter is a boolean variable that indicates whether the action
        being performed is a jump or not. If `is_jump` is `True`, it means that the action is a jump
        """
        if is_jump:
            self._jump()
        self._animate()
