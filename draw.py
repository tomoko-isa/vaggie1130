"""描画関連の関数群"""
import js

# キャンバスを取得 --- (*1)
canvas = js.document.getElementById("canvas")
ctx = canvas.getContext("2d")

# 画像の読み込み用変数 --- (*2)
images = []  # 野菜イラストのリスト
image_load_count = 0  # 読み込み済みイラスト数

def load_images():
    """野菜のイラストを読み込む"""
    def on_image_load(e):
        global image_load_count
        image_load_count = image_load_count + 1
        if image_load_count == 9:
            # 画像を9枚ロードしたらスタートボタンを有効化する --- (*3)
            q("#start-button").disabled = False
    # 9枚の連番の画像を読み込む --- (*4)
    for i in range(1, 9 + 1):
        img = js.Image.new()
        images.append(img)
        img.addEventListener("load", on_image_load)
        img.src = f"./images/card{i}.png"

load_images()  # 画像を読み込む --- (*5)

def draw_veggie_list(veggie_list, price_list, selected_list):
    """野菜リストを描画する関数"""  # --- (*6)
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    for row in range(3):
        for col in range(3):
            x = col * CARD_W  # カードの表示位置(x座標)を計算 --- (*7)
            y = row * CARD_H  # カードの表示位置(y座標)を計算
            id = row * 3 + col  # リストのインデックスを計算
            image = images[veggie_list[id]]  # 野菜イラストを取得
            ctx.drawImage(image,
                0, 0, image.width, image.height,
                x, y, CARD_W, CARD_W,
            )  # 野菜の画像を描画 --- (*8)
            price = price_list[id]  # 価格を取得
            # 画像の下に価格のテキストを描画 --- (*9)
            ctx.font = "16px 'Arial'"
            ctx.fillStyle = "black"
            ctx.fillText(f"{price}円", x + 40, y + CARD_W + 15)
            if selected_list[id]:  # 選択されている場合は枠を描画 --- (*10)
                ctx.lineWidth = 3
                ctx.strokeStyle = "navy"
                ctx.strokeRect(x + 3, y + 3, CARD_W - 6, CARD_W - 6)

def draw_price_list(price_list):
    """価格リストを描画する関数"""  # --- (*11)
    draw_veggie_list(list(range(9)), price_list, [False] * 9)