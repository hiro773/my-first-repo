book = {
    "title": "python入門",
    "author": "山田太郎"
}
book["year"] = 2024
print(book["title"])
print(book["author"])
for key, value in book.items():
    print(key,",",value)