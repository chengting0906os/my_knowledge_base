def fun(*args, **kwargs):
    print(args)
    print(kwargs)


if __name__ == "__main__":
    fun(1, 2, 3, name="test", age="18")

"""
(1, 2, 3)
{'name': 'test', 'age': '18'}

args 接收多個位置參數（positional arguments），打包成 tuple
kwargs 接收多個 keyword arguments，打包成 dict

PS:
Positional argument：按位置傳入，順序決定對應哪個參數。
Keyword argument：用參數名稱指定，順序不重要。
"""
