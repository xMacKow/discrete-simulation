import pygame
import re

VALUE_NAMES = ['name', 'armour', 'hp', 'attack', 'defence', 'speed']


# Wczytuje z danej linii, obcina białe znaki,
# zamienia numery na inty i zwraca tablice
def get_line_data(line_num, file):
    f = open(file, 'r')
    line = f.readlines()[line_num]
    f.close()
    split = line.split(',')
    for index, string in enumerate(split):
        split[index] = string.rstrip()
        if re.match(r"^[-+]?[0-9]+$", string):
            split[index] = int(string)

    return split


# CZYTANIE Z PLIKU
class Troop:
    ally = True

    def __init__(self, x, y, number, line_num, file):
        self.x = x
        self.y = y
        self.vX = 0
        self.vY = 0
        self.number = number
        for index, value in enumerate(get_line_data(line_num, file)):
            if type(value) is str:
                exec('self.{} = "{}"'.format(VALUE_NAMES[index], value))
            elif type(value) is int:
                exec('self.{} = {}'.format(VALUE_NAMES[index], value))

    def print_values(self):
        print("Printing parameters for: {}".format(self.name))
        print("Position: ({},{}) - size: {}".format(self.x, self.y, self.get_size()))
        for value in VALUE_NAMES[1:]:
            print("{} - {}".format(value, getattr(self, value)))

    def damage(self, enemyAttackValue):
        if self.number == 0:
            pass

        self.number -= (enemyAttackValue * (100 - self.armour) * 0.1)
        if self.number < 0:
            self.number = 0

    def update(self):
        raise NotImplementedError("Update on parent class")

    def stop(self):
        self.vX = 0
        self.vY = 0

    def move(self, closestEnemy):
        if closestEnemy.x + closestEnemy.get_size() / 2 < self.x:
            self.vX = -(self.speed / 10)
        elif closestEnemy.x + closestEnemy.get_size() / 2 >= self.x:
            self.vX = (self.speed / 10)

        if closestEnemy.y + closestEnemy.get_size() / 2 < self.y:
            self.vY = -(self.speed / 10)
        elif closestEnemy.y + closestEnemy.get_size() / 2 >= self.y:
            self.vY = (self.speed / 10)

        self.x += self.vX
        self.y += self.vY

    def get_size(self):
        return (self.number * self.hp) / 10000

    def draw(self, screen, ally):
        color = (50, 50, 200) if not ally else (200, 50, 50)
        rect = pygame.draw.rect(screen, color, (self.x, self.y, self.get_size(), self.get_size()))


class LightCavalry(Troop):
    def __init__(self, x, y, number, line_num=1, file='dane.csv'):
        super().__init__(x, y, number, line_num, file)

    def draw(self, screen, ally):
        super().draw(screen, ally)


class TatarCavalry(Troop):
    def __init__(self, x, y, number, line_num=7, file='dane.csv'):
        super().__init__(x, y, number, line_num, file)

    def draw(self, screen, ally):
        super().draw(screen, ally)


class Cossack(Troop):
    def __init__(self, x, y, number, line_num=8, file='dane.csv'):
        super().__init__(x, y, number, line_num, file)

    def draw(self, screen, ally):
        super().draw(screen, ally)


class Infantry(Troop):
    def __init__(self, x, y, number, line_num=2, file='dane.csv'):
        super().__init__(x, y, number, line_num, file)

    def draw(self, screen, ally):
        super().draw(screen, ally)


class TatarInfantry(Troop):
    def __init__(self, x, y, number, line_num=6, file='dane.csv'):
        super().__init__(x, y, number, line_num, file)

    def draw(self, screen, ally):
        super().draw(screen, ally)


class SpearMan(Troop):
    def __init__(self, x, y, number, line_num=3, file='dane.csv'):
        super().__init__(x, y, number, line_num, file)

    def draw(self, screen, ally):
        super().draw(screen, ally)


class Archer(Troop):
    def __init__(self, x, y, number, line_num=4, file='dane.csv'):
        super().__init__(x, y, number, line_num, file)

    def draw(self, screen, ally):
        super().draw(screen, ally)


class Hussar(Troop):
    def __init__(self, x, y, number, line_num=5, file='dane.csv'):
        super().__init__(x, y, number, line_num, file)

    def draw(self, screen, ally):
        super().draw(screen, ally)
