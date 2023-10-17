# Payton Lutterman
# Snake-Food-Class
# Last Updated 10-11

from scripts.settings import *

class Food(object):
    def __init__(self, game):
        self.game = game
        x = random.randint(0, (WIDTH - TIlE_SIZE)//TIlE_SIZE-1)*TIlE_SIZE
        y = random.randint(0, (HEIGHT - TIlE_SIZE)//TIlE_SIZE-1)*TIlE_SIZE
        self.coordinates = [x,y]

        # Creating The Food Shape and Size
        self.game.canvas.create_oval(x,y, x+TIlE_SIZE, y + TIlE_SIZE, fill=FOOD_COLOR, tag="food")
