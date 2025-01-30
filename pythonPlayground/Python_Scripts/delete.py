class Person:
    name = "Lily"
    def __init__(self, age):
        self.age = age

    def myfunc(self):
        print(f"Hello my name is { Person.name}  {self.age}")

p1 = Person(36)
p1.myfunc()
