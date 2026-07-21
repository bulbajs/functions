#===== Task 10 =====
# Game Character + Weapon Сделай: Weapon: damage
# Character:name self.weapon = Weapon(...) метод attack() использует урон оружия
class Weapon():
    def __init__(self, damage = 100):
        self.damage = damage

class Character():
    def __init__(self, name):
        self.name = name
        self.weapon = Weapon()

    def attack(self):
        print(f'Атака {self.name} составляет {self.weapon.damage} урона')

    def info(self):
        print(f'Вы выбрали персонажа {self.name}')

print('---ДОБРО ПОЖАЛОВАТЬ В ИГРУ---')
print('---ГЕНДАЛЬФ НА КОНЕ---')
char1 = Character('Gendalf')
char1.info()
char1.attack()