class Animal:
    def __init__(self, name="animal"):
        self.name=name
        self.eyes=2
        self.legs=4

    def walk(self):
        print(self.name, "walking on 4 legs...")

class Spider(Animal):
    def __init__(self, name="spider"):
        super().__init__()
        self.name=name
        self.color="black"

    def walk(self):
        print("spider is crawling....")

elephant=Animal()
spider=Spider()
# elephant.walk()
# spider.walk()

for animal in [elephant, spider]:
    animal.walk()