# 文件操作
# # 打开文件
# f = open("resources/text1.txt", "r", encoding="utf-8")
#
# # 读文件
# content = f.read()
# print(content)
#
# content_list = f.readlines()
# for line in content_list:
#     print(line.strip())
#
# # 关闭文件
# f.close()

# 打开文件
f = open("resources/text2.txt", "w", encoding="utf-8")

try:
    # 写文件（方式一）
    f.write("啦啦啦啦啦啦啦啦啦啦啦啦啦")
finally:
    # 关闭文件
    f.close()

# 写文件（方式二）
with open("resources/text2.txt", "r", encoding="utf-8") as f:
    f.write("啦啦啦啦啦啦啦啦啦啦啦啦啦")
