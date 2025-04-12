import pygame
from constants import *

class Button:
    def __init__(self, position, text="BUTTON", action=None, font=None, color=BUTTON_COLOR, hover_color=BUTTON_HOVER_COLOR):
        self.position = position
        self.text = text
        self.font = font or pygame.font.SysFont(None, 30)
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.text_surface = self.font.render(text, True, BLACK_COLOR)
        self.text_rect = self.text_surface.get_rect()
        self.padding = 10
        self.rect = pygame.Rect(
            position[0],
            position[1],
            self.text_rect.width + (self.padding * 2),
            self.text_rect.height + (self.padding * 2)
            )
        self.text_rect.center = self.rect.center

    def draw(self, surface, is_selected=False):
        if is_selected:
            color = BUTTON_HOVER_COLOR
        else:
            color = self.hover_color if self.is_hovered() else self.color
        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, LIGHT_GREY_COLOR, self.rect, 2)
        surface.blit(self.text_surface, self.text_rect)

    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def click(self):
        if self.is_hovered():
            if self.action:
                return self.action().upper().replace(" ", "_")    
