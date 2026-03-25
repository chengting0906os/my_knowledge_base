"""
import demo，觀察 __name__ 的差異
"""
import demo   # ← 這時 demo.py 裡的 __name__ == 'demo'，不是 '__main__'

print(f"\n目前 __name__ = {__name__!r}")   # '__main__'（main.py 自己）

# 可以正常使用 demo 裡定義的函式
print(demo.add(10, 20))       # 30
print(demo.greet("Bob"))      # Hello, Bob!

# if __name__ == '__main__' 那段「不會」被執行
