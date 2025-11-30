import js
import random

# 定数 --- (*1)
CANVAS_W = 390  # キャンバスの幅
CARD_W = CANVAS_W // 3  # カードの幅
CARD_H = CARD_W + 20  # カードの高さ + ラベル表示部分
MEMORY_TIME = 3000  # 価格を表示する時間（ミリ秒）
GOAL_PRICE = 1000  # 目標価格
# グローバル変数 --- (*2)
price_list = []  # 価格リスト
veggie_list = []  # 野菜リスト
selected_list = []  # 選択されたカードのリスト

def game_start(e):
    """ゲーム開始"""  # --- (*3)
    global price_list
    # スタートボタンを有効にして、お会計エリアを非表示に --- (*4)
    q("#start-button").disabled = True
    q("#checkout-area").style.display = "none"
    # 価格リストを作成してシャッフル --- (*5)
    price_list = list(range(300, 300 + 9 * 50, 50))
    list_shuffle(price_list)
    # 価格リストを表示して、MEMORY_TIMEミリ秒後に買い物ターンへ --- (*6)
    draw_price_list(price_list)
    q_text("#info", f"{int(MEMORY_TIME/1000)}秒で価格を覚えてね！")
    set_timeout(shopping_turn, MEMORY_TIME)

def shopping_turn():
    """買い物ターン開始"""  # --- (*7)
    global veggie_list, selected_list
    # リストに並ぶ野菜を9個選ぶ
    veggie_list = [random.randint(0, 8) for _ in range(9)]
    selected_list = [False] * 9
    draw_veggie_list(veggie_list, ["???"] * 9, selected_list)
    q_text("#info", f"合計{GOAL_PRICE}円になるように野菜を選んで!")
    # お会計エリアを表示
    q("#checkout-area").style.display = "block"

def checkout(event):
    """お会計"""  # --- (*8)
    global selected_list
    # 選択された野菜の合計金額を計算 
    total = 0
    for i in range(9):
        if selected_list[i]:
            total += price_list[veggie_list[i]]
    # 結果を表示 ---- (*9)
    if total == GOAL_PRICE:
        q_text("#info", f"素晴らしい！合計はピッタリ{GOAL_PRICE}円でした！")
    elif total > GOAL_PRICE:
        q_text("#info", f"残念。合計は{total}円で予算をオーバーしました！")
    elif total > (GOAL_PRICE - 100):
        q_text("#info", f"合格！合計は{total}円で、ほぼ1000円でした！")
    else:
        q_text("#info", f"残念。合計は{total}円でした。もっと買えたのに…")
    # スタートボタンを有効化して、お会計エリアを非表示に --- (*10)
    q("#start-button").disabled = False
    q("#checkout-area").style.display = "none"
    draw_veggie_list(veggie_list, [price_list[i] for i in veggie_list], selected_list)
    selected_list = []  # クリックできないように調整