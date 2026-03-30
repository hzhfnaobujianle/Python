# # 登录功能
# ok_account = "123456"
# ok_password = "123456"
#
# account = input("请输入你的账号：")
# password = input("请输入您的密码：")
#
# if account == ok_account and password == ok_password:
#     print("登录成功")
# else:
#     print("登录失败，账号或密码错误")
#
# # 判断数字
# num = int(input("请输入num:"))
# if num > 0:
#     print(f"{num}是正数")
# elif num == 0:
#     print(f"{num}是0")
# else:
#     print(f"{num}是负数")

# 三角形判断
a = int(input("三角形的第一条边的边长："))
b = int(input("三角形的第二条边的边长："))
c = int(input("三角形的第三条边的边长："))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("等边三角形")
    elif a == b or a == c or b == c:
        print("等腰三角形")
    else:
        print("普通三角形")
else:
    print("不构成三角形")
