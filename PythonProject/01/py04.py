# 算术运算符 + - * / // % **
print("10 + 4 = ", 10 + 4)  # 加法
print("10 - 4 = ", 10 - 4)  # 减法
print("10 * 4 = ", 10 * 4)  # 乘法
print("10 / 4 = ", 10 / 4)  # 除法
print("10 // 4 = ", 10 // 4)  # 整除
print("10 % 4 = ", 10 % 4)  # 取余
print("10 ** 4 = ", 10 ** 4)  # 幂

# 算术优先级 ** --> * / // % --> + -

# 赋值运算符
# += -= *= /= /= //= %= **=
num = 85
num += 10
print("num += 10后，num的值为：", num)  # 95
num -= 10
print("num -= 10后，num的值为：", num)  # 85
num *= 10
print("num *= 10后，num的值为：", num)  # 850
num /= 10
print("num /= 10后，num的值为：", num)  # 85.0
num //= 10
print("num //= 10后，num的值为：", num)  # 8.0
num %= 3
print("num %= 3后，num的值为：", num)  # 2.0
num **= 3
print("num **= 3后，num的值为：", num)  # 8.0

# 比较运算符
# == != > >= < <=
print("100 == 100", 100 == 100)
print("100 != 100", 100 != 100)
print("100 > 100", 100 > 100)
print("100 >= 100", 100 >= 100)
print("100 < 100", 100 < 100)
print("100 <= 100", 100 <= 100)

# 逻辑运算符 and or not
# 案例1
num = int(input("请输入一个整数："))
print(f"{num}在10-20之间：", 10 <= num and num <= 20)
print(f"{num}在10-20之间：", 10 <= num <= 20)

# 案例2
num = int(input("请输入一个整数："))
print(f"{num}不在10-20之间：", 10 > num or num > 20)
