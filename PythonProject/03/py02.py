# 字符串 str
# 不可变性（无法修改） 有序性 可迭代性

s = "Hello-Python"
print(s)
print(s[4])  # 正向索引
print(s[-8])  # 反向索引

for i in s:
    print(i)

print(s[0:5:1])
print(s[:5:1])
print(s[:5:])

print(s[6:12:1])
print(s[6::1])

print(s[-1:-7:-1])

# 常用方法
s = "Hello-Python-Hello-World"

index = s.find("-")  # 查找指定字符第一次出现的位置
print(index)

c = s.count("o")  # 指定字符计数
print(c)

s.upper()  # 转为大写
print(s)

s.lower()  # 转为小写
print(s)

slist = s.split("-")  # 将字符按照指定字符串切割
print(slist)

ss = s.strip()  # 去除字符串两端空格
print(ss)

sr = s.replace("-", "_")  # 将字符串的指定字符替换成新的内容
print(sr)

print(s.startswith("Hello"))  # 字符串是否以指定的字符串开始
print(s.endswith("Python"))  # 字符串是否以指定的字符串结束

print("-------------------------")
print(s)

# 案例
mail = input("请输入邮箱：")

if mail.count("@") == 1 and "." in mail:
    print("合法邮箱")
else:
    print("非法邮箱")
