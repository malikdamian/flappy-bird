from os import walk

import pygame
from pygame import Surface


WIDTH, HEIGHT = 600, 650

pipe_pair_sizes = [
    (1, 7),
    (2, 6),
    (3, 5),
    (4, 4),
    (5, 3),
    (6, 2),
    (7, 1),
]

pipe_size = HEIGHT // 10
pipe_gap = (pipe_size * 2) + (pipe_size // 2)
ground_space = 50


def import_sprite(path: str) -> list[Surface]:
    """
    Loads all images in that path using Pygame, 
    converts them to alpha surfaces, and returns a list of these surfaces.

    :param path: Path where the sprite images are located
    :return: A list of pygame Surface objects
    """
    surface_list: list[Surface] = []

    for _, _, image_file in walk(path):
        for image in image_file:
            full_path = f"{path}/{image}"
            image_surface: Surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)
            
    return surface_list
