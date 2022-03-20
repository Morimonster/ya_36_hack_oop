import random


class Thing:
    """Кдасс вещей."""
    
    def __init__(self, 
                thing_name,
                thing_armor, 
                thing_damage) -> None:
        self.thing_name = thing_name
        self.thing_armor = thing_armor
        self.thing_damage = thing_damage
    
    def show_thing(self):
        print(f'Вид амуниции: {self.thing_name};\n'
              f'Очки брони: {self.thing_armor};\n'
              f'Очки урона: {self.thing_damage}')

    

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

class DressedWarrior(Person, Thing):
    """Создание одетого персонажа."""

    def dressed_man(self):
        print(f'Имя персонажа: {self.name};\n'
              f'Статус персонажа: {self.status};\n'
              f'Вид амуниции: {self.thing_name};\n'
              f'Здоровье: {self.hp};\n'
              f'Атака: {self.attack + self.thing_damage};\n'
              f'Защита: {self.armor + self.thing_armor}')






pers_name_list = ['Джейд', 'Бор', 'Снэйк', 'Спайк', 'Джасп', 'Скео', 'Рольф', 'Зик', 'Локи', 'Стэлс']
pers_rand_name = random.choice(pers_name_list)
#print(pers_rand_name)

pers_status = ['Паладин', 'Воин']
pers_rand_status = random.choice(pers_status)
#print(pers_rand_status)

base_hp = 100
base_attack = 10
base_armor = 8

if pers_rand_status == 'Паладин':
    base_hp *= 2
    if pers_rand_status == 'Паладин':
        base_armor *= 2
elif pers_rand_status == 'Воин':
    base_attack *= 2

fighter = Person(str(pers_rand_name), 
            str(pers_rand_status), 
            base_hp, 
            base_attack, 
            base_armor)


base_thing_armor = 0
base_thing_attack = 0

thing_list = ['Меч', 'Лук', 'Щит', 'Броник', 'Шлем']
rand_thing_name = random.choice(thing_list)


if rand_thing_name == 'Меч':
    base_thing_attack = 10
elif rand_thing_name == 'Лук':
    base_thing_attack = 15
elif rand_thing_name == 'Щит':
    base_thing_armor = 8
elif rand_thing_name == 'Броник':
    base_thing_armor = 12
elif rand_thing_name == 'Шлем':
    base_thing_armor = 10

thing = Thing(rand_thing_name,
            base_thing_armor,
            base_thing_attack)




Person.show_person(fighter)
Thing.show_thing(thing)




        