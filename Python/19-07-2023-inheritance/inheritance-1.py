class Animal:
    def __init__(self, name="test"):
        self.name=name
        self.eyes=2
        self.legs=4

class Spider(Animal):
    def __init__(self):
        super().__init__(name="spider")
        self.name="balalalaa"
        self.color="black"


black_window=Spider()
tarantula=Spider()
turtle=Spider()

print("spider: ", black_window.name)
print("spider:", tarantula.name)

elephant=Animal()

print("animal:", elephant.name)