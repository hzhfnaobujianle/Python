# 字面量
print(100)  # 整数类型(int)
print(3.14)  # 浮点数类型(float)
print(True)  # 布尔类型(bool)
print(False)
print("hello python")  # 字符串类型(str)
print("------------")
print(None)  # 空值(NoneType)

print(True + 1)  # 2
print(False - 1)  # -1

# 变量
num = 1114.1
print(num)

num = num + 1
print(num)

num = "OK"
print(num)

num = True
print(num)

# 案例
# base = 20.7  # 基础播放量
# incr = 50  # 每一个月的新增播放量
base, incr = 20.7, 50
print("未来第一个月的播放总量：", base + incr)
print("未来第二个月的播放总量：", base + incr + incr)

# 变量交换
a = 10
b = 20

c = a
a = b
b = c

print(a, b)
