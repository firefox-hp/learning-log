day = 2
goal = "做出3个自动化小工具"
print(type("你好"))   # str 文字
print(type(2))        # int 整数
print(type(3.14))     # float 小数
print(type(True))     # bool 真/假
print(f"今天是第{day}天，目标：{goal}")
a = input("数字1：")
b = input("数字2：")
print(a + b)            # 输入 1 和 2，得到 12，不是 3
print(int(a) + int(b))  # 转成整数再加，得到 3
print(7 + 2, 7 - 2, 7 * 2)
print(7 / 2)    # 3.5
print(7 // 2)   # 3，整除
print(7 % 2)    # 1，余数
print(2 ** 3)   # 8，次方