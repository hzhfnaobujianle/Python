# 变量的作用域

# 全局变量 局部变量
num = 100


def circle_area(r):
    area = 3.14 * r ** 2
    global num
    num = 10000
    print("num = ", num)
    return area


print(circle_area(10))
print("num = ", num)


# 传参方式
def student_1(name, age, gender, city):
    print(f"注册成功，姓名：{name}，年龄：{age}，性别：{gender}，城市：{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}


# 位置参数
stu1 = student_1("张三", 18, "男", "上海")
print(stu1)

# 关键字参数
stu2 = student_1(name="王林", age=21, gender="男", city="上海")
print(stu2)

# 位置参数 + 关键字参数
stu3 = student_1("李慕婉", 19, gender="女", city="北京")
print(stu3)


# 缺省参数
def student_2(name, age, gender, city="深圳"):
    print(f"注册成功，姓名：{name}，年龄：{age}，性别：{gender}，城市：{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}


stu4 = student_2("李四", 19, "男")
print(stu4)

stu5 = student_2("王五", 20, "男", "北京")
print(stu5)


# 不定长参数--位置传递
def calc_data(*args):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)
    return min_data, max_data, round(avg_data, 1)


print(calc_data(2, 7, 9, 10, 45))


# 不定长参数--关键字传递
def calc_data(*args, **kwargs):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)

    if kwargs.get("round") is not None:
        avg_data = round(avg_data, kwargs.get("round"))
    if kwargs.get("print") is not None:
        print(min_data, max_data, avg_data)
    return min_data, max_data, avg_data


print(calc_data(2, 7, 9, 10, 45, 111, 121, round=3, print=True))


# 函数的参数类型
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calc(a, b, oper):
    return oper(a, b)


result = calc(10, 20, add)
print(result)


# 匿名函数
# lambda 参数列表:函数体
def out_line():
    print("--------------")


outline = lambda: print("--------------")
outline()


def add(a, b):
    return a + b


add2 = lambda a, b: a + b
print(add2(10, 20))

# 案例
data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
print(data_list)
data_list.sort(key=lambda item: len(item))
print(data_list)
data_list.sort(key=lambda item: len(item), reverse=True)
print(data_list)
