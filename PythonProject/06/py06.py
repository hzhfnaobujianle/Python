# 异常处理
try:
    print("================")
    # print(my_name)
    # print(1 / 0)
    # print("ABC"[10])
    print("ABC".hello)
    print("================")
except NameError as e:
    print("名字不存在，请检查变量或函数的名字，异常信息:", e)
except ZeroDivisionError as e:
    print("0不能做被除数，异常信息:", e)
except IndexError as e:
    print("索引错误，异常信息:", e)
except Exception as e:
    print("运行出错，请联系管理员，异常信息:", e)
finally:
    print("释放资源~")


# 异常传递
# 异常的传递
def fun1():
    print("fun1 ... running ...")
    fun2()


def fun2():
    print("fun2 ... running ...")
    fun3()


def fun3():
    print("fun3 ... running ...")
    print(my_color)


if __name__ == '__main__':
    try:
        fun1()
    except NameError as e:
        print("程序出错啦，请联系管理员，异常信息：", e)
