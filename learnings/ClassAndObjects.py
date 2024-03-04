class Dog:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def __str__(self):
        return "Dog\n" + "name: " + self._name + "\nage: " + str(self._age)

    def random():
        return 7

# Creating the object instance
d1 = Dog("Scruffy", 5)
print(d1)

# Calling the non-static method
print(Dog.random())


