import pygame
import sys

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300
PLAYER_MOVE_SPEED = 200
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN = 0.3

SHOT_RADIUS = 5

# Game Menus
MAIN_MENU_OPTIONS = ["Start Game", "Instructions", "Options", "Exit"]

# Game States
GAME_STATE = {
    1: "MAIN MENU", 
    2: "PLAYING",
    3: "PAUSE_MENU", 
    4: "CONTINUE MENU", 
    5: "BUY MENU", 
    6: "INSTRUCTIONS", 
    7: "OPTIONS", 
    8: "GAME_OVER"}

#  Resource Indecies
RESOURCES = {
    0: "Credits",
    1: "Silica",
    2: "Iron",
    3: "Aluminum",
    4: "Cobalt",
    5: "Gold",
    6: "Uranium",
    7: "Thorium",
    8: "Level",
    9: "XP",
    10: "XP to Next Level"
}

CREDITS = 0
SILICA = 1
IRON = 2
ALUMINUM = 3
COBALT = 4
GOLD = 5
URANIUM = 6
THORIUM = 7

# Asteroid Colors
SILICA_COLOR = (194,178,128), # Sand
IRON_COLOR = (185,78,72), # Deep Chestnut
ALUMINUM_COLOR =  (145,163,176), # Cadet Grey
COBALT_COLOR = (176,196,222), # Light Steel Blue
GOLD_COLOR =  (218,165,32), # Goldenrod
URANIUM_COLOR = (173,255,47), # Green Yellow
THORIUM_COLOR = (135,206,235), # Sky Blue

# Other Colors
WHITE_COLOR = (255, 255, 255) # White
GRAY_COLOR = (128, 128, 128) # Gray
BLACK_COLOR = (0, 0, 0) # Black
BUTTON_COLOR= (100, 100, 100)
BUTTON_HOVER_COLOR = (200, 200, 200)
LIGHT_GREY_COLOR = (200, 200, 200)

def emergency_exit():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LCTRL] and keys[pygame.K_q]:
        pygame.quit()
        sys.exit()