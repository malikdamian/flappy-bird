import pygame
from pygame import Surface

from settings import WIDTH

pygame.font.init()


class GameIndicator:
    def __init__(self, screen: Surface) -> None:
        self.screen = screen
        self.font = pygame.font.SysFont("Bauhaus 93", 60)
        self.inst_font = pygame.font.SysFont("Bauhaus", 30)
        self.color = pygame.Color("white")
        self.inst_color = pygame.Color("black")

    def show_score(self, int_score) -> None:
        bird_score = str(int_score)
        score = self.font.render(bird_score, True, self.color)
        self.screen.blit(score, (WIDTH // 2, 50))

    def instructions(self) -> None:
        inst_text1 = "Press SPACE button to Jump"
        inst_text2 = "Press \"R\" Button to Restart Game"
        ins1 = self.inst_font.render(inst_text1, True, self.inst_color)
        ins2 = self.inst_font.render(inst_text2, True, self.inst_color)
        self.screen.blit(ins1, (160, 400))
        self.screen.blit(ins2, (120, 450))
