# 集合 set
# 无序 不可重复（自动去重） 可修改

# 定义
s1 = {5, 3, 2, 0, 9, 12, 43, 64, 22, 5, 0}
print(s1)
print(type(s1))

s2 = set()  # 定义空集合
print(s2)
print(type(s2))

# 常用方法
s1 = {100, 200, 300, 400, 500, 600, 700, 800}
print(s1)

s1.add(1200)  # 添加新元素到集合
print(s1)

s1.remove(200)  # 移除集合中的指定元素
print(s1)

e = s1.pop()  # 随即删除集合中的元素并返回
print(e)
print(s1)

s1.clear()  # 清除集合
print(s1)

s2 = {"A", "B", "C", "D", "E", "X", "Y"}
s3 = {"C", "E", "Y", "Z"}

print(s2.difference(s3))  # 求两个集合的差集
print(s3.difference(s2))

print(s2.union(s3))  # 求两个集合的并集
print(s3.union(s2))

print(s2.intersection(s3))  # 求两个集合的交集
print(s2.intersection(s2))

# 案例
football_set = {"张三", "李四", "王五", "赵六", "钱七", "孙八", "周九", "吴十", "郑十一"}
basketball_set = {"王五", "赵六", "小红", "小明", "小雨", "小林", "小华", "小晨", "小阳"}
french_set = {"李四", "王五", "小明", "小红", "小刚", "小丽", "小亮", "小美"}
art_set = {"王五", "赵六", "小红", "小丽", "小雨", "小雪", "小宇", "小琳", "小泽", "小琪"}

fa_set1 = french_set.intersection(art_set)
print("同时选修了法语和艺术：", fa_set1)

fa_set2 = french_set & art_set
print("同时选修了法语和艺术：", fa_set2)

all_set = football_set & basketball_set & french_set & art_set
print("同时选修了四门课的：", all_set)

fb_set1 = football_set.difference(basketball_set)
print("选修了足球没有选修篮球：", fb_set1)

fb_set2 = football_set - basketball_set
print("选修了足球没有选修篮球：", fb_set2)

fb_set3 = {s for s in football_set if s not in basketball_set}
print("选修了足球没有选修篮球：", fb_set3)

# all_set = football_set.union(basketball_set).union(french_set).union(art_set)
all_set = football_set | basketball_set | french_set | art_set
print(all_set)

all_list = [*football_set, *basketball_set, *french_set, *art_set]
for s in all_set:
    print(f"{s} 选修了 {all_list.count(s)} 课程")
