price = float(input("请输入原价："))
discount = float(input("请输入折扣（8 表示八折，8.2 表示 8.2 折）："))
result = round(price * discount / 10, 2)
print(f"折后价：{result}")