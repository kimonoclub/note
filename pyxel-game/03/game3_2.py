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
        self.player = Player(32, 32)
        pyxel.run(self.update, self.draw)

    def update(self):
                
        # True と False の切り替え
        self.player.step = not self.player.step


    # ここで画像を表示しています
    def draw(self):
        pyxel.cls(0)
        # pyxel.blt(32, 32, 0, ここをどう書くかが問題だ, 0, 8, 8, 0)
        time.sleep(0.3)

App()
