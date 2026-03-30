# 类型推断--动态类型语言
a = 596
score = 98.5
hobby = "Python"
flag = True
pic = None

names = ["A", "C", "E"]
phones = {"13309091111", "15209101902", "18809019201"}
options = {"count": 2, "total": 10}
goods = ("手机", 6999, 1)

# 类型注解--提示
a2: int = 596
score2: float = 98.5
hobby2: str = "Python"
flag2: bool = True
pic2: None = None

names2: list[str] = ["A", "C", "E"]
phones2: set[str] = {"13309091111", "15209101902", "18809019201"}
options2: dict[str, int] = {"count": 2, "total": 10}
goods2: tuple[str, int, int] = ("手机", 6999, 1)


# 函数的类型注解
def calc_order_list(*args: tuple[str, float, int], coupon: int = 0, score: int = 0, express: float = 0.0) -> float:
    """
    :param args: 商品信息（商品名、价格、数量）
    :param coupon: 优惠券
    :param score: 积分抵扣
    :param express: 运费
    :return: 订单总金额
    """
    order_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(order_price)
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon
    if total_cost >= 5000 and score // 100 <= total_cost:
        total_cost -= score // 100
    total_cost += express
    return total_cost


total = calc_order_list(("鼠标", 188, 2), ("键盘", 388, 1), ("手机", 6999, 1), coupon=10, score=4000, express=9.9)
print(total)
