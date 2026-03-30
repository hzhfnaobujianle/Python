# 定义类--不推荐
class Car:
    pass


# 创建对象
car = Car()
# 动态地为对象添加属性
car.color = "red"
car.brand = "BMW"
car.name = "X5"
car.price = 500000

print(car)
print(car.__dict__)


# 定义类--推荐
class Car:
    def __init__(self, color, brand, name, price):
        self.color = color
        self.brand = brand
        self.name = name
        self.price = price


# 创建对象
car = Car("red", "BMW", "X5", 500000)
print(car)
print(car.__dict__)
