# Payton Lutterman
# Snake-Settings
# Last Updated 10-11

from tkinter import *
from tkinter import ttk
from tkinter import font
import random
import pygame as pg
from PIL import ImageTk, Image
from tkinter import messagebox

pg.mixer.init()
TITLE = "Snake"
WIDTH = 800
HEIGHT = 800
FPS = 200
CELLS = 12
TIlE_SIZE = WIDTH // CELLS
BODY_PARTS = 2
SNAKE_COlOR = "green"
FOOD_COLOR = "red"
BG_COlOR = "black"
geo_string = str(WIDTH) + "x" + str(HEIGHT)
ICON = ("assets/imgs/snakes.ico")