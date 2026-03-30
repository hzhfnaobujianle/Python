# 元组 tuple
# 不可修改！！！

# 定义
t1 = (80, 95, 78, 50, 76, 80, 85, 20)
# t1 = 80, 95, 78, 50, 76, 80, 85, 20
print(t1)
print(type(t1))

# 索引访问
print(t1[0])
print(t1[-1])

# 切片
print(t1[0:5:1])

print(t1.count(80))  # 指定元素技术

print(t1.index(80))  # 指定元素第一次出现的位置

t2 = ()  # 空元组
print(t2)
print(type(t2))

t3 = (100,)  # 元组中只有一个元素
print(t3)
print(type(t3))

t1 = (5, 7, 9, 10, 2, 23, 12)
t2 = 5, 7, 9, 10, 2, 23, 12

print(t1)
print(t2)

# 解包操作
a, b, c, d, e, f, g = t1
print(a, b, c, d, e, f, g)

first, second, *other, third = t1
print(first, second, other, third)

*other, last2, last1 = t1
print(other)
print(last1, last2)

# 案例（组包与解包）
a = 10
b = 20

a, b = b, a
print(a, b)

# 案例
students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周佚", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)

# 计算每个学生的总分，各科平均分，并输出
print(f"学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
for s in students:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    print(f"{s[0]}\t{s[1]}\t\t{s[2]}\t\t{s[3]}\t\t{s[4]}\t\t{total}\t\t{avg:.1f}")

# 统计各科成绩的最高分，最低分，平均分并输出
chinese_scores = [s[2] for s in students]
print(chinese_scores)
math_scores = [s[3] for s in students]
english_scores = [s[4] for s in students]

print(f"语文最高分{max(chinese_scores)},最低分{min(chinese_scores)},平均分{sum(chinese_scores) / len(chinese_scores)}")
print(f"数学最高分{max(math_scores)},最低分{min(math_scores)},平均分{sum(math_scores) / len(math_scores)}")
print(f"英语最高分{max(english_scores)},最低分{min(english_scores)},平均分{sum(english_scores) / len(english_scores)}")

# 查询成绩优秀（成绩大于90分）的学生，并输出
print("优秀学生名单如下：")
for s in students:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    if avg > 90:
        print(f"{s[1]}  {avg:.1f}")

# 案例（元组解包）
students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周佚", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)

# 计算每个学生的总分，各科平均分，并输出
print(f"学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
for id, name, chinese, math, english in students:
    total = chinese + math + english
    avg = total / 3
    print(f"{id}\t{name}\t\t{chinese}\t\t{math}\t\t{english}\t\t{total}\t\t{avg:.1f}")

# 统计各科成绩的最高分，最低分，平均分并输出
chinese_scores = [s[2] for s in students]
print(chinese_scores)
math_scores = [s[3] for s in students]
english_scores = [s[4] for s in students]

print(f"语文最高分{max(chinese_scores)},最低分{min(chinese_scores)},平均分{sum(chinese_scores) / len(chinese_scores)}")
print(f"数学最高分{max(math_scores)},最低分{min(math_scores)},平均分{sum(math_scores) / len(math_scores)}")
print(f"英语最高分{max(english_scores)},最低分{min(english_scores)},平均分{sum(english_scores) / len(english_scores)}")

# 查询成绩优秀（成绩大于90分）的学生，并输出
print("优秀学生名单如下：")
for id, name, chinese, math, english in students:
    total = chinese + math + english
    avg = total / 3
    if avg > 90:
        print(f"{name}  {avg:.1f}")
