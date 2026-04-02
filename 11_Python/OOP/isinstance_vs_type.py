class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()

print(type(d) == Animal)
print(type(d) == Dog)
print(isinstance(d, Animal))
print(isinstance(d, Dog))
