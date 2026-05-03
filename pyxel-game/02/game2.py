import pyxel

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.step = True
    
class App:
    def __init__(self):
        pyxel.init(64, 64)
        
        # 💡 対策1：画像の読み込み
        # HTML経由の場合は、ファイル名だけだと見失うことがあるため、try-exceptで保護します
        try:
            pyxel.load("character.pyxres")
        except:
            print("リソースファイルが見つかりません")
            
        self.player = Player(0, 32)
        pyxel.run(self.update, self.draw)

    def update(self):
        # 💡 修正2：time.sleepの代わりに「フレーム数」を使う
        # pyxel.frame_count は起動してから1/30秒ごとに1ずつ増える数字です
        # 10フレーム（約0.3秒）ごとに足を切り替えるようにします
        if pyxel.frame_count % 10 == 0:
            self.player.step = not self.player.step
        
        # せっかくなので、少しずつ右に歩かせてみましょう（任意）
        self.player.x = (self.player.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        # キャラクターの描画
        # 💡 対策3：もし画像が読み込めていなくてもエラーで止まらないようにしています
        pyxel.blt(self.player.x, self.player.y, 0, 0 if self.player.step else 8, 0, 8, 8, 0)

# 💡 修正4：Web公開時のお作法
if __name__ == "__main__":
    App()