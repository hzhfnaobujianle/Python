import json

# 写入json文件
user = {
    "username": "whj",
    "password": "123456",
    "email": "3163238826@163.com",
    "hobbies": ["reading", "studying"]
}
with open("resources/user.json", "w", encoding="utf-8") as f:
    json.dump(user, f, ensure_ascii=False, indent=4)  # 序列化

# 读取json文件
with open("resources/user.json", "r", encoding="utf-8") as f:
    user = json.load(f)  # 反序列化
    print(user)
    print(type(user))
