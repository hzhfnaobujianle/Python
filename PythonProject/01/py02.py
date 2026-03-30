# type()--获得指定字面量或变量的类型
print(type("hello"))
print(type(10))
print(type(3.14))
print(type(True))
print(type(None))

num = 100
print(type(num))

# isinstance(数据，类型)--判定数据类型是否是指定类型
print(isinstance(num, int))
print(isinstance(num, float))
print(isinstance(num, bool))

# 字符串的定义
s1 = "hello"
s2 = 'python'
s3 = """
    welcome!
"""

print(s1)
print(s2)
print(s3)

# 转义字符 \' \" \n \t
msg1 = 'It\'s very good!'
print(msg1)

msg2 = "It's very good!"
print(msg2)

print("\twelcome\n\teveryone!")

# 字符串拼接
s1 = "welcome"
s2 = "everyone"
s3 = 123
print(s1 + "," + s2 + str(s3))

# 字符串的格式化
name = "whj"
age = 22
major = "cs"
print("大家好，我是" + name + ",年龄是" + str(age) + ",专业是" + major)
print("大家好，我是%s,年龄是%d,专业是%s" % (name, age, major))
print(f"大家好，我是{name},年龄是{age},专业是{major}")
