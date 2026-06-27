import pygame
import json
import os
import math

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mobs idle")
clock = pygame.time.Clock()


BG = (18, 18, 24)
SURFACE = (28, 28, 38)
SURFACE2 = (38, 38, 52)
WHITE = (220, 220, 230)
MUTED = (120, 120, 140)
GOLD = (186, 117, 23)
RED = (200, 60, 60)
GREEN = (60, 180, 100)
BLUE = (50, 130, 220)
ORANGE = (210, 100, 40)
LOCKED = (60, 60, 75)
TAB_ACTIVE = (50, 130, 220)

font_big = pygame.font.Sysfont("segoeui", 28, bold=True)
font_med = pygame.font.Sysfont("segoeui", 18)
font_small = pygame.font.Sysfont("segoeui", 14)
font_tiny = pygame.font.Sysfont("segoeui", 12)

SAVE_FILE = "save.json"

MOB_NAMES = ["Slime", "Goblin", "Orc", "Troll", "Dark knight", "Shadow beast",
             "Demon lord", "Ancient dragon"]

UPGRADES = {
    "attack":[
        {"id":"atk1","name":"Sharpened Blade","desc":"+2 dmg / level","max":5,
         "base_cost":15,"mult":2.2,"requiere":None,"req_lvl":0,"effect":"damage","value":2},
        {"id":"atk2","name":"Heavy Strikes", "dessc":"+5 dmg / level","max":4,"base_cost":120,
             "mult":2.8,"requieres":"atk1","req_lvl":3,"effect":"damage","value":5},
        {"id":"atk3","name":"Berserker Rage", "desc":"+15 dmg / level","max":3,"base_cost":1200,
         "mult":3.5,"requiere":"atk2","req_lvl":2,"effect":"damage","value":15},
    ],
    "speed": [
        {"id":"spd1","name":"Quick Hands", "desc":"-20% attack interval / level", "max":5,
         "base_cost":25,"mult":2.4,"requieres":None,"req_lvl":0,"effect":"speed", "value":0.80},
        {"id":"spd2","name":"Combat Rhythm", "desc":"-30% attack interval / level","max":3,
          "base_cost":300,"mult":3.0,"requieres":"spd1","req_lvl":3,"effect":"speed","value":0.70},
        {"id":"spd3","name":"Blur of Motion", "desc":"-40% attack interval / level","max":2,
         "base_cost":2500,"mult":4.0,"requieres":"spd2","req_lvl":2,"effect":"speed","value":0.60},
    ],
    "gold":[
        {"id":"gld1","name":"Looter Instinct","desc":"+25% gold / level","max":5,
         "base_cost":40,"mult":2.5,"requieres":None,"req_lvl":0,"effect":"gold","value":0.25},
        {"id":"gld2","name":"Treasure Sense","desc":"+60% gold / level","max":3,
         "base_cost":400,"mult":3.2,"requieres":"gld1","req_lvl":2,"effect":"gold","value":0.60},
        {"id":"gld3","name":"Legendary Hoard","desc":"+150% gold / level","max":2,
         "base_cost":3500,"mult":4.5,"requieres":"gld2","req_lvl":2,"effect":"gold","value":1.50},
    ],
    "crit":[
        {"id":"crt1","name":"Lucky Strike","desc":"+5% crit chance / level","max":4,
         "base_cost":80,"mult":2.6,"requieres":None,"req_lvl":0,"effect":"crit_chance","value":5},
        {"id":"crt2","name":"Vital Points","desc":"+3x crit mult / level","max":3,
         "base_cost":500,"mult":3.3,"requieres":"crt1","req_lvl":2,"effect":"crit_mult","value":3},
        {"id":"crt3","name":"Execution Strike","desc":"+10% crit chance / level","max":2,
         "base_cost":4000,"mult":5.0,"requieres":"ctr2","req_lvl":2,"effect":"crit_chance","value":10},
    ],
} 