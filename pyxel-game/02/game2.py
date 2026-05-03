import pyxel
import time

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.step = True
    
class App:
    def __init__(self):
        pyxel.init(64, 64)
        pyxel.load("character.pyxres")
        self.player = Player(0, 32)
        pyxel.run(self.update, self.draw)

    def update(self):
                
        self.player.step = not self.player.step


    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.player.x, self.player.y, 0, 0 if self.player.step else 8, 0, 8, 8, 0)
        time.sleep(0.3)

App()
