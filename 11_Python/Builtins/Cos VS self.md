**What is the difference between self and cls?**

The main difference between self and cls is the types of methods they denote. Class methods use cls while instance methods use self. A class acts as the blueprint for building an object, and an instance is a specific copy of that object.


class Car:  # 這是藍圖(Class)
    wheels = 4  # 類別屬性(所有車都有的特性)
    
    def __init__(self, color):
        self.color = color  # 實例屬性(每台車獨有的特性)
    
    def drive(self):  # 實例方法 - 用 self
        print(f"The {self.color} car is driving")
    
    @classmethod
    def get_wheels(cls):  # 類別方法 - 用 cls
        return cls.wheels

# 創建實例(具體的車子)
car1 = Car("red")    # 紅色車 - 一個實例
car2 = Car("blue")   # 藍色車 - 另一個實例

car1.drive()  # self = car1
car2.drive()  # self = car2

Car.get_wheels()  # cls = Car(類別本身)