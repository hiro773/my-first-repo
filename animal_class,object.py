class animal:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def introduce(self):
        print(f"{self.name}は{self.kind}に分類される動物です")

animal1 = animal("トカゲ", "爬虫類")
animal1.introduce()