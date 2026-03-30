class Car:
    # 类属性
    wheel = 4  # 轮胎数量
    tax_rate = 0.1  # 购置税

    def __init__(self, brand, name, price):
        # 实例属性
        self.brand = brand
        self.name = name
        self.price = price

    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶...")

    def total_cost(self, discount, rate=0.1):
        """
        :param discount:  折扣
        :param rate: 税率
        :return: 提车总费用
        """
        return self.price * discount + self.price * rate


c1 = Car("BYD", "汉", 180000)
print(c1)
print(c1.brand)
print(c1.wheel)
print(Car.wheel)

c2 = Car("Tesla", "Model Y", 260000)
print(c2)
