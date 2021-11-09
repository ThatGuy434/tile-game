import pygame as pg
vec = pg.math.Vector2

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap"
BGCOLOR = DARKGREY

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# PLayer settings
PLAYER_HEALTH = 200
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 200
PLAYER_IMG = 'tank_blue.png'
WALL_IMG = "crateMetal.png"
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(25, 0)

# gun settings
BULLET_IMG = "bulletBlue2.png"
BULLET_SPEED = 500
BULLET_LIFETIME = 1000
BULLET_RATE = 150
KICKBACK = 200
GUN_SPREAD = 5
BULLET_DAMAGE = 10

# mob settings
MOB_IMG = "tankBody_red.png"
MOB_SPEED = [150, 125, 100]
MOB_HIT_RECT = pg.Rect(0, 0, 35, 35)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
AVOID_RADIUS = 50

# Effects
MUZZLE_FLASHES = ['explosion2.png', 'explosion4.png', 'explosionSmoke2.png', 'explosionsmoke4.png']
FLASH_DURATION = 40

# Layers
WALL_LAYER = 1
PLAYER_LAYER = 2
MOB_LAYER = 2
BULLET_LAYER = 3
EFFECTS_LAYER = 4
ITEM_LAYER = 1

# Items
ITEM_IMAGES = {'health': 'barrelGreen_side.png'}
HEALTH_PACK_AMOUNT = 20
