import pygame
import math
from constants import *
class Game:
    def __init__(self):
        self.resources = [
            0, # credits
            0, # silica
            0, # iron
            0, # aluminum
            0, # cobalt
            0, # gold
            0, # uranium
            0 # thorium
        ]
        self.level = 1
        self.xp = 0
        self.next_level = 10
        self.is_running = False
        self.is_paused = False

    def score_keeper(self, target_tier):
        self.resources[target_tier] += 1
        self.xp += target_tier
        self.resources[CREDITS] += target_tier * 2
        if self.xp >= self.next_level:
            self.level += 1
            self.xp = 0
            self.next_level += math.floor(self.level * 1.2)
        print(f"Level: {self.level}, XP: {self.xp}, Next Level: {self.next_level}")
        print(f"Resources: {self.resources}")
        print(f"Credits: {self.resources[CREDITS]}")