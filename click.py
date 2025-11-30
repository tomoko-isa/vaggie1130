"""画面クリックした時の処理"""
def on_canvas_click(event):
    """キャンバスがクリックされた時の処理"""  # --- (*1)
    if len(selected_list) == 0:  # ゲームが始まっていない状態
        return
    # クリック位置を取得 --- (*2)
    rect = canvas.getBoundingClientRect()
    x = event.clientX - rect.left
    y = event.clientY - rect.top
    # クリックされた位置を計算 --- (*3)
    gx, gy = int(x // CARD_W), int(y // CARD_H)
    if gx < 0 or gx >= 3 or gy < 0 or gy >= 3:
        return
    # クリックされたカードの選択状態を反転して再描画 --- (*4)
    selected_id = gy * 3 + gx
    selected_list[selected_id] = not selected_list[selected_id]
    draw_veggie_list(veggie_list, ["???"] * 9, selected_list)

# クリックイベントを登録 --- (*5)
q("#canvas").addEventListener("click", on_canvas_click)