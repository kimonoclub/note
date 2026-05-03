import pyxel

RIGHT = 0
LEFT  = 1
DOWN  = 2
UP    = 3

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.step = True
        self.orientation = RIGHT

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
class App:


    
    def __init__(self):
        pyxel.init(64, 64)
        pyxel.load("character.pyxres")
        self.player = Player(32, 32)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_UP):
            self.player.move(0, -4)
            self.player.orientation = UP
            self.player.step = not self.player.step
            
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.player.move(0, 4)
            self.player.orientation = DOWN
            self.player.step = not self.player.step
            
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.player.move(4, 0)
            self.player.orientation = RIGHT
            self.player.step = not self.player.step
            
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.player.move(-4, 0)
            self.player.orientation = LEFT
            self.player.step = not self.player.step
        
    def draw(self):
        pyxel.cls(0)

        pyxel.blt(self.player.x, self.player.y,
                  0,
                  0 if self.player.step else 8,
                  self.player.orientation * 8,
                  8, 8, 0)

App()
