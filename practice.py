# 辞書の作成
person = {
    "name": "Taro",
    "age": 25,
    "job": "designer"
}

# 値を取り出す
print(person["name"])   # → Taro

# 値を変更する
person["age"] = 30

# 新しいキーと値を追加
person["city"] = "Tokyo"

# 辞書の中身を全部見る
for key, value in person.items():
    print(key, ":", value)