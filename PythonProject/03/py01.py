# 列表 list
# 特点：可以存储不同类型的元素，元素有序，可以重复，可以修改
# 索引：正向索引（从前向后），从0开始；反向索引（从后向前），从-1开始

# 列表操作
# 定义
s = [56, 90, 88, 65, 90, "A", "hello", True]
print(type(s))

# 访问列表元素
# 获取
print(s[0])  # 正向索引
print(s[-8])  # 反向索引

# 修改
s[5] = "ABC"
print(s)

# 删除
del s[-2]
print(s)

# 遍历
for item in s:
    print(item)

# 切片 list[开始索引，结束索引，步长]
s = ["A", "C", "H", "K", "L", "B", "D", "X", "C", "U"]

# ['A', 'C', 'H', 'K', 'L']
print(s[0:5:1])
print(type(s[0:5:1]))
print(s[:5:1])
print(s[:5:])
print(s[:5])

print(s[0:5:2])

print(s[0:-2:2])

# 常见方法
s = [56, 90, 88, 100, 209, 72, 145]
print(s)

s.append(188)  # 在列表结尾追加元素
print(s)

s.insert(2, 80)  # 在指定元素前插入元素
print(s)

s.remove(90)  # 移除第一个匹配到的元素
print(s)

e = s.pop(1)  # 删除列表中指定位置的元素并返回
print(e)

e = s.pop()  # 若未指定，则默认删除最后一个
print(e)
print(s)

s.sort()  # 排序
print(s)

s.reverse()  # 反转列表元素
print(s)

# 案例1
num_list = []
for i in range(10):
    num = int(input("请输入一个数字："))
    num_list.append(num)
print(num_list)

num_list.sort()
print("排序后：", num_list)
print("最大值：", num_list[-1])  # max()
print("最小值", num_list[0])  # min()
print("平均值：", sum(num_list) / len(num_list))

# 案例2
num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

# 合并
for num in num_list2:
    num_list1.append(num)
print("合并后的原始列表：", num_list1)

# 去重
new_list = []
for num in num_list1:
    if num not in new_list:  # 元素 in 列表 (bool)
        new_list.append(num)
print("去重后的列表：", new_list)

# 案例2（简化1）
num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

# 合并
# 解包：将列表这一容器解开成一个一个独立的元素
# 组包：将多个值合并到一个容器
num_list = [*num_list1, *num_list2]
print("合并后的原始列表：", num_list)

# 去重
new_list = []
for num in num_list1:
    if num not in new_list:
        new_list.append(num)
print("去重后的列表：", new_list)

# 案例2（简化2）
num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

# 合并
num_list = num_list1 + num_list2
print("合并后的原始列表：", num_list)

# 去重
new_list = []
for num in num_list1:
    if num not in new_list:
        new_list.append(num)
print("去重后的列表：", new_list)

# 案例3
# 方式一
num_list1 = []
for i in range(1, 21):
    num_list1.append(i ** 2)
print(num_list1)

# 方式二 列表推导式
num_list2 = [i ** 2 for i in range(1, 21)]
print(num_list2)

# 案例4
num_list = [12, 32, 45, 77, 80, 92, 33, 57, 97, 98, 110, 111, 122]
new_list = [i ** 2 for i in num_list if i % 2 == 0]
print(new_list)
