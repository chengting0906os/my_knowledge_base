class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2


c = Circle(5)
print(c.radius)
print(c.area)
c.radius = 10
