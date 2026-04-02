class Card:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value


a = Card(1)
b = Card(1)

print(a == b)
print(hash(a))
my_set = {a, b}
