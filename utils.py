import js
import random

def q(query):
    """簡単にHTML要素を取得する関数"""  # --- (*1)
    return js.document.querySelector(query)

def q_text(query, text):
    """テキストを設定する関数"""  # --- (*2)
    q(query).innerText = text

def set_timeout(f, ms):
    """タイマーを設定する関数"""  # --- (*3)
    return js.setTimeout(f, ms)

def list_shuffle(a_list):
    """リストをシャッフルする関数"""  # --- (*4)
    for i in range(len(a_list) - 1, 0, -1):
        j = random.randint(0, i)
        a_list[i], a_list[j] = a_list[j], a_list[i]