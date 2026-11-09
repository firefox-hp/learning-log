chinese = float(input("请输入语文成绩："))
math = float(input("请输入数学成绩："))
english = float(input("请输入英语成绩："))

total = chinese + math + english
average = round(total / 3, 2)
print(f"总分：{total}")
print(f"平均分：{average}")