"""
1) Вещи: class Thing Класс содержит в себе следующие параметры - название, процент защиты, атаку и жизнь; Это могут быть предметы одежды, магические кольца, всё что угодно)

2) Персонаж: class Person Класс, содержащий в себе следующие параметры:

    Имя, кол-во hp/жизней, базовую атаку, базовый процент защиты. Параметры передаются через конструктор;
    метод, принимающий на вход список вещей set_things(things);
    метод вычитания жизни на основе входной атаки, а также методы для выполнения алгоритма, представленного ниже;
3) Паладин: class Paladin Класс наследуется от персонажа, при этом количество присвоенных жизней и процент защиты умножается на 2 в конструкторе;

4) Воин: class Warrior Класс наследуется от персонажа, при этом атака умножается на 2 в конструкторе./


"""
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
                hp = 100,
                attack = 10,
                armor = 8) -> None:
        self.name = name
        self.hp = hp
        self.attack = attack
        self.armor = armor

    def set_things(self):
        pass

class Paladin(Person):
    def __init__(self, 
                name, 
                hp, 
                attack, 
                armor) -> None:
        super().__init__(name, 
                        hp, 
                        attack, 
                        armor)
        self.hp *= 2
        self.attack += 10
        self.armor *= 2


class Warrior(Person):
    def __init__(self, 
                name, 
                hp=100, 
                attack=10 * 2, 
                armor=8) -> None:
        super().__init__(name, 
                        hp, 
                        attack, 
                        armor)
        self.attack *= 2               
    def show_pers(self):
        return (f'Имя: {self.name}, HP: {self.hp}, Атака: {self.attack}, Защита: {self.armor}')

def get_parameters(par):
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




        