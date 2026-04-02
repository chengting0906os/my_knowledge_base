class Fighter:
    def attack(self):
        print("punch")

    def attack(self, weapon):
        print(f"attack with {weapon}")


f = Fighter()

try:
    f.attack()
except TypeError:
    pass

f.attack("sword")
