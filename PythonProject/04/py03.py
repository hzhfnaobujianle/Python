# 计算n的阶乘
def jc(n):
    if n == 1:
        return 1
    else:
        return n * jc(n - 1)


print(jc(10))


# 电商订单计算器
def calc_order_list(*args, coupon=0, score=0, express=0.0):
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
