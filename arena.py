"""
1) Вещи: class Thing Класс содержит в себе следующие параметры - название, процент защиты, атаку и жизнь; Это могут быть предметы одежды, магические кольца, всё что угодно)

2) Персонаж: class Person Класс, содержащий в себе следующие параметры:

    Имя, кол-во hp/жизней, базовую атаку, базовый процент защиты. Параметры передаются через конструктор;
    метод, принимающий на вход список вещей set_things(things);
    метод вычитания жизни на основе входной атаки, а также методы для выполнения алгоритма, представленного ниже;
3) Паладин: class Paladin Класс наследуется от персонажа, при этом количество присвоенных жизней и процент защиты умножается на 2 в конструкторе;

4) Воин: class Warrior Класс наследуется от персонажа, при этом атака умножается на 2 в конструкторе./


"""
import random
from unicodedata import name


class Thing:
    """Кдасс вещей."""
    
    def __init__(self, 
                thing_name,
                thing_armor, 
                thing_damage) -> None:
        self.thing_name = thing_name
        self.thing_armor = thing_armor
        self.thing_damage = thing_damage
    

class Person:
    """Класс персонажа."""


    def __init__(self, 
                name,
                status,
                hp,
                attack,
                armor) -> None:
        self.name = name
        self.status = status
        self.hp = hp
        self.attack = attack
        self.armor = armor
        
    def show_person(self):
        print(f'Имя персонажа: {self.name};\n'
                f'Статус персонажа: {self.status};\n'
                f'Здоровье: {self.hp};\n'
                f'Атака: {self.attack};\n'
                f'Защита: {self.armor}')

    def set_things(self):
        pass


pers_name_list = ['Jade', 'Bore', 'Snake', 'Spike', 'Jasp', 'Skeo', 'Rolf', 'Zik', 'Loki', 'Clans']
pers_rand_name = random.choice(pers_name_list)
#print(pers_rand_name)

pers_status = ['Paladin', 'Warrior']
pers_rand_status = random.choice(pers_status)
#print(pers_rand_status)

base_hp = 100
base_attack = 10
base_armor = 8

if pers_rand_status == 'Paladin':
    base_hp *= 2
    if pers_rand_status == 'Paladin':
        base_armor *= 2
elif pers_rand_status == 'Warrior':
    base_attack *= 2

t = Person(str(pers_rand_name), 
            str(pers_rand_status), 
            base_hp, 
            base_attack, 
            base_armor)

Person.show_person(t)




"""def get_parameters(par):
    params = {
        'name': 'Bob',
        'hp': 100,
        'attack': 10,
        'armor': 8
        }
    print(params[par])
    
base_pars = [('name'), ('hp'), ('attack'), ('armor')]
for par in base_pars:
    get_parameters(par)


get_parameters(par)
"""



        