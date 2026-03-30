# # 登录
# while True:
#     username = input("请输入正确的用户名：")
#     password = input("请输入正确的密码：")
#
#     if username == "" or password == "":
#         print("用户名或密码不能为空！")
#         continue  # 结束当前循环，进入下一轮循环
#
#     if username == "admin" and password == "123456":
#         print("登录成功！")
#         break  # 直接退出循环
#     else:
#         print("用户名或密码错误")


# 猜数字
import random

random_num = random.randint(1, 100)  # 生成随机数

while True:
    num = int(input("请输入一个数字："))
    if num > random_num:
        print("big!")
        continue
    elif num < random_num:
        print("small!")
        continue
    else:
        print("yes!")
        break

print("生成的随机数是：", random_num)
