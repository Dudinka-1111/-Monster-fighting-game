#Пример результата:
#Боец выбирает меч.
#Боец наносит удар мечом.
#Монстр побежден!
#Боец выбирает лук.
#Боец наносит удар из лука.
#Монстр побежден!

#Исходные данные:
#Есть класс Fighter, представляющий бойца.
#Есть класс Monster, представляющий монстра.
#Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.

#Шаг 1: Создайте абстрактный класс для оружия
#Создайте абстрактный класс Weapon, который будет содержать абстрактный метод attack().

from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

#Шаг 2: Реализуйте конкретные типы оружия
#Создайте несколько классов, унаследованных от Weapon, например, Sword и Bow.
#Каждый из этих классов реализует метод attack() своим уникальным способом.

class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

#Шаг 3: Модифицируйте класс Fighter
#Добавьте в класс Fighter поле, которое будет хранить объект класса Weapon.
#Добавьте метод change_weapon(), который позволяет изменить оружие бойца.

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon
        weapon_name = "меч" if isinstance(weapon, Sword) else "лук"
        print(f"{self.name} выбирает {weapon_name}.")

    def attack(self):
        if self.weapon:
            print(self.weapon.attack())
            print("Монстр побежден!")
        else:
            print("Боец безоружен!")

class Monster:
    def __init__(self, name):
        self.name = name

#Шаг 4: Реализация боя

def main():
    fighter = Fighter("Боец")

    # Выбор меча и атака
    sword = Sword()
    fighter.change_weapon(sword)
    fighter.attack()

    # Выбор лука и атака
    bow = Bow()
    fighter.change_weapon(bow)
    fighter.attack()


if __name__ == "__main__":
    main()