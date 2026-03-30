# # 遍历字符串
# msg = input("请输入需要遍历的字符串：")
#
# for s in msg:
#     print(f"元素：{s}")
# else:
#     print("结束")

# range(start, end, step)

# # 案例 计算1-100之间的所有奇数之和
# total = 0
# for i in range(1, 101):
#     if i % 2 == 1:
#         total += i
# print(f"1-100之间的所有奇数之和: {total}")
#
# # 简化
# total = 0
# for i in range(1, 101, 2):
#     total += i
# print(f"1-100之间的所有奇数之和: {total}")

# 打印九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i} x {j} = {i * j}", end="\t")
    print( )

