# Payton Lutterman
# Snake-Class
# Last Updated 10-11

from scripts.settings import *

class Snake(object):
    def __init__(self,game):
        self.game = game
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(self.body_size):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square = self.game.canvas.create_rectangle(x,y, x+TIlE_SIZE, y+TIlE_SIZE, fill=SNAKE_COlOR)
            self.squares.append(square)