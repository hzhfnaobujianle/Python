# 字典 dict
# key:value key不可重复，可修改

dict1 = {"王林": 670, "李慕婉": 608, "徐立国": 580, "韩立": 688}
print(dict1)
print(type(dict1))

dict2 = {}
print(dict2)
dict3 = dict()
print(dict3)

# 访问
print(dict1["李慕婉"])  # 获取
dict1["李慕婉"] = 688  # 修改
print(dict1)

# 常用方法
dict1 = {"王林": 670, "李慕婉": 608, "徐立国": 580, "韩立": 688}
print(dict1)

dict1["whj"] = 552  # 添加
print(dict1)

dict1["whj"] = 650  # 修改
print(dict1)

print(dict1["whj"])  # 查询
print(dict1.get("whj"))

print(dict1.keys())
print(dict1.values())
print(dict1.items())

score = dict1.pop("徐立国")  # 删除并返回值
print(score)
print(dict1)

del dict1["韩立"]  # 删除
print(dict1)

# 遍历
for k in dict1.keys():
    print(f"{k}: {dict1[k]}")

for k, v in dict1.items():
    print(f"{k}: {v}")

# 案例 购物车管理系统
shopping_cart = {}

menu = """
########  购物车系统  ########
        1. 添加购物车
        2. 修改购物车
        3. 删除购物车
        4. 查询购物车
        5. 退出购物车
"""

print("欢迎使用购物车管理系统~")
print(menu)

while True:
    choice = input("请选择要执行的操作（1-5）：")
    match choice:
        case "1":  # 添加
            goods_name = input("请输入商品的名称：")
            goods_price = float(input("请输入商品的价格："))
            goods_num = int(input("请输入商品的数量："))
            if goods_name in shopping_cart:
                print("该商品已存在~")
            else:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("商品添加完成~")
        case "2":  # 修改
            goods_name = input("请输入新的商品的名称：")
            if goods_name not in shopping_cart:
                print("该商品不存在，请重新选择~")
                continue
            goods_price = float(input("请输入新的商品的价格："))
            goods_num = int(input("请输入新的商品的数量："))
            shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
            print("商品修改完成~")
        case "3":  # 删除
            goods_name = input("请输入要删除商品的名称：")
            if goods_name not in shopping_cart:
                print("该商品不存在，请重新选择~")
            else:
                del shopping_cart[goods_name]
                print("商品删除完成~")
        case "4":  # 查询
            for goods_name in shopping_cart.keys():
                goods_info = shopping_cart[goods_name]
                print(f"商品名称：{goods_name}，商品价格：{goods_info['price']}，商品数量：{goods_info['num']}")
        case "5":  # 退出
            print("Bye~")
            break
        case _:
            print("非法操作")
