class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print("I an {} and I am {} years old".format(self.name,self.age))

    def make_sound(self):
        print("I bark at strangers")

class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print("I am {} and I am {} years old".format(self.name,self.age))

    def make_sound(self):
        print("I pur when i want to drink")

d1=Dog("Coco",10)
c1=Cat("Kitty",8)

for animal in d1,c1:
    animal.info()
    animal.make_sound()