# 计算1-100的偶数之和
total = 0
i = 1

while i <= 100:
    if i % 2 == 0:
        total += i
    i+=1

print(f"1-100的偶数之和为：{total}")
