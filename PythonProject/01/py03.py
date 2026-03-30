# 输入与输出
# name = input("请输入您的姓名：")
# age = input("请输入你的年龄：")
#
# print(f"我是{name},年龄是{age}岁")

# 案例：银行ATM取款
# 总金额
total = 10000
# 1.输入密码
password = input("请输入您的银行卡密码：")
print(f"密码正确，{password}")
# 2.输入取款金额
num = input("请输入您的取款金额：")
# 3.计算余额并输出
print(f"取款后银行卡余额为：{total - int(num)}")
