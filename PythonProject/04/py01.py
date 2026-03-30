# 函数定义

def on_line():
    print("-------------")


# 函数调用
on_line()


# 函数的参数与返回值
# 计算圆的面积--半径
def circle_area(r):
    area = 3.14 * r ** 2
    return area


area = circle_area(5)
print(area)


# 长方形的面积--长 宽
def rectangle_area(l, w):
    area = l * w
    return area


area = rectangle_area(5, 3)
print(area)


# 计算圆的面积和周长--半径
def circle_area_len(r):
    return round(3.14 * r ** 2, 1), round(2 * 3.14 * r, 1)


al = circle_area_len(5)  # 多个返回值会封装到元组中
print(al)
print(type(al))

area, length = circle_area_len(5)
print(area)
print(length)


# 函数的嵌套调用
def function_a():
    print("a_before")
    function_b()
    print("a_after")


def function_b():
    print("b_before")
    function_c()
    print("b_after")


def function_c():
    print("c")


function_a()
