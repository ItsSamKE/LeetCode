
class Dog:
    # In Python, self is a special variable that is used to refer to the current instance of a class. It is the first argument to every method in a class and is used to access the attributes and methods of the class within the method.

    # Self is a conventional name for the first argument of a instance method.  It is used to refer to the instance of the object itself. You don't have to call it self, you can name it whatever
    # An __init__ is a special method in python that is called when an instance of the class is created. It is a constructor method that is used to initialize the attributes of an instance.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Bark is an instance method that prints a greeting using the instance's name attribute
    def bark(self):
        print(f"Hello, my name is {self.name} and i bark")

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age


d = Dog('Bosco', 12)
d.bark()
d.setAge(19)
print(d.getAge())
# print(type(d))
