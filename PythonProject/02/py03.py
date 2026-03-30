# day = input("请输入星期几（1-7）：")
#
# match day:
#     case "1":
#         print("周一")
#     case "2":
#         print("周二")
#     case "3":
#         print("周三")
#     case "4":
#         print("周四")
#     case "5":
#         print("周五")
#     case "6":
#         print("周六")
#     case "7":
#         print("周日")
#     case _:
#         print("输入有误")

# 四则计算器
num1 = int(input("请输入第一个操作数："))
num2 = int(input("请输入第二个操作数："))
op = input("请输入运算符（+ - * /）：")

match op:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1}  *{num2} = {num1 * num2}")
    case "/" if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    case _:
        print("操作数不支持")
