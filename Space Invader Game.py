import math
import random
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_Y = 4
ENEMY_SPEED_X = 40
BULLET_SPEED_Y = 10
COLLISON_DISTANCE = 27

pygame.init()

screen = pygame.display.set_mode((800, 500))

pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

player = pygame.image.load('Rocket.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

enemy = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy.append(pygame.image.load('Enemy.png'))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

bullet = pygame.image.load('Bullet.png')
bulletX = 0
bulletY = PLAYER_START_Y
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"
