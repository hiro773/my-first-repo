class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"こんにちは、私は{self.name}です。{self.age}歳です。")

# クラスを使う
person1 = Person("山田太郎", 25)
person1.greet()
