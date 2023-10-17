# Payton Lutterman
# Snake-Game-Class
# Last Updated 10-11

from scripts.settings import *
from scripts.classes.food_class import Food
from scripts.classes.snake_class import Snake

class Game(object):
    def __init__(self):
        self.score = 0
        self.pg = pg
        self.dir = random.choice(['down',"right"])
        self.pg.mixer.init()
        self.sfx_list = []
        self.load_sfx()
        self.root_setup()
        self.create_widgets()
        self.setup_game()
        self.pg.mixer.music.play(loops=-1)


    def setup_game(self):
        self.canvas.delete(ALL)
        self.dir = "down"
        self.food = Food(self)
        self.snake = Snake(self)
        self.score = 0
        self.header.config(text="Score: {}".format(self.score))
        self.root.after(FPS, self.tick)

    def play(self):
        self.root.mainloop()

    def create_widgets(self):
        self.header = Label(self.root, text="Score: {}".format(self.score), font="consolas 40 bold")
        self.canvas = Canvas(self.root, bg=BG_COlOR, width=WIDTH, height=HEIGHT)
        self.header.pack()
        self.canvas.pack()

    def load_sfx(self):
        paths = ["assets/sfx/background.mp3",
                 "assets/sfx/death.mp3",
                 "assets/sfx/eatapple.mp3"]

        for name in paths:
            self.sfx_list.append(pg.mixer.Sound(name))
        self.pg.mixer.music.load("assets/sfx/background.mp3")

    def root_setup(self):
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.geometry(geo_string)
        self.root.title(TITLE)
        self.root.iconbitmap(ICON)
        self.root.bind("<Left>", lambda event:self.change_dir("left"))
        self.root.bind("<Right>", lambda event:self.change_dir("right"))
        self.root.bind("<Up>", lambda event: self.change_dir("up"))
        self.root.bind("<Down>", lambda event: self.change_dir("down"))
        self.root.bind("<a>", lambda event: self.change_dir("left"))
        self.root.bind("<d>", lambda event:self.change_dir("right"))
        self.root.bind("<w>", lambda event: self.change_dir("up"))
        self.root.bind("<s>", lambda event: self.change_dir("down"))

    def tick(self):
        x,y = self.snake.coordinates[0]
        if self.dir == 'up':
            y -=  int(TIlE_SIZE)
        elif self.dir == 'down':
            y += int(TIlE_SIZE)
        elif self.dir == 'left':
            x -= int(TIlE_SIZE)
        elif self.dir == 'right':
            x += int(TIlE_SIZE)
        self.snake.coordinates.insert(0,(x,y))
        sq = self.canvas.create_rectangle(x,y, x+TIlE_SIZE, y+TIlE_SIZE, fill=SNAKE_COlOR)
        self.snake.squares.insert(0, sq)
        # Checking if Snake Hits Food
        if x == self.food.coordinates[0] and y == self.food.coordinates[1]:
            self.score += 1
            pg.mixer.Sound.play(self.sfx_list[2])
            self.header.config(text="Score {}".format(self.score))
            self.canvas.delete('food')
            self.food = Food(self)
        else:
            del self.snake.coordinates[-1]
            self.canvas.delete(self.snake.squares[-1])
            del self.snake.squares[-1]

        # If food spawns offscreen destroy it and make a new one
        if ((self.food.coordinates[0] < 0 or self.food.coordinates[0] > WIDTH)
                or (self.food.coordinates[1] < 0 or self.food.coordinates[1] > HEIGHT)):
            self.canvas.delete('food')
            self.food = Food(self)

        if self.check_collisions() == True:
            self.game_over()
            return

        self.root.after(FPS,self.tick)

    def check_collisions(self):
        x, y = self.snake.coordinates[0]
        # Checking if the snake goes offscreen
        if (x < 0 or x > WIDTH) or (y < 0 or y > HEIGHT):
            return True
        # Checking if Snake hits itself
        for BODY_PARTS in self.snake.coordinates[1:]:
            if x == BODY_PARTS[0] and y == BODY_PARTS[1]:
                return True
        return False

    def game_over(self):
        pg.mixer.music.fadeout(1500)
        pg.mixer.Sound.play(self.sfx_list[1])
        self.canvas.delete(ALL)
        self.canvas.create_text(WIDTH/2, HEIGHT*.25, text="YOU LOSE", font="consolas 70 bold", fill='red', tag='gameover')
        answer = messagebox.askyesno('Game Over', 'Would You Like To Play Again?')
        if answer:
            self.root.after(2500, self.setup_game())
        else:
            self.root.after(2500, self.root.destroy())

    def change_dir(self, dir):
        if dir == 'left':
            if self.dir != 'right':
                self.dir = dir
        elif dir == 'right':
            if self.dir != 'left':
                self.dir = dir
        elif dir == 'down':
            if self.dir != 'up':
                self.dir = dir
        elif dir == 'up':
            if self.dir != 'down':
                self.dir = dir