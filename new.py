class Human:
    def __init__(self, name: str, age: int, work: str):
        self.name = name
        self.age = age
        self.work = work

    def greetings(self):
        return f'{self.name}, Hi'


zhan = Human()
stone = Human()
zhan.name = 'Zhan'
print(zhan.name)
print(zhan.greetings())
