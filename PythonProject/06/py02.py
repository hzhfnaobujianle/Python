class Car:
    def __init__(self, brand, name, price):
        self.brand = brand
        self.name = name
        self.price = price

    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶...")

    def total_cost(self, discount, rate):
        """
        :param discount:  折扣
        :param rate: 税率
        :return: 提车总费用
        """
        return self.price * discount + self.price * rate


car = Car("BMW", "X5", 500000)
total_cost = car.total_cost(0.9, 0.1)
print(f"提车总价为：{total_cost:.0f}")
car.running()
