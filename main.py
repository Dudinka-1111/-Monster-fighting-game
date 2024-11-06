from abc import ABC, abstractmethod


# Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


# Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."


class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."


# Класс бойца
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


# Пример использования
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