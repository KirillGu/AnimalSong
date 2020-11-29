class Cow:
    type_animal = 'Корова'

    def __init__(self, name, weight, sound, milk):
        self.name = name
        self.weight = weight
        self.sound = sound
        self.milk = milk



class Ducks:
    type_animal = 'Утка'

    def __init__(self, name, weight, sound, eggs):
        self.name = name
        self.weight = weight
        self.sound = sound
        self.eggs = eggs



class Geese:
    type_animal = 'Гусь'

    def __init__(self, name, weight, sound, eggs):
        self.name = name
        self.weight = weight
        self.sound = sound
        self.eggs = eggs



class Goats:
    type_animal = 'Коза'

    def __init__(self, name, weight, sound, milk):
        self.name = name
        self.weight = weight
        self.sound = sound
        self.milk = milk



class Hens:
    type_animal = 'Курица'

    def __init__(self, name, weight, sound, eggs):
        self.name = name
        self.weight = weight
        self.sound = sound
        self.eggs = eggs



class Sheep:
    type_animal = 'Баран'

    def __init__(self, name, weight, sound, wool):
        self.name = name
        self.weight = weight
        self.sound = sound
        self.wool = wool



class Far:
    def __init__(self, farm):
        self.farm = farm

    def get_heavy(self):
        heavy = ''
        max_weight = 0

        for item in self.farm:
            if item.weight > max_weight:
                max_weight = item.weight
                heavy = f"{item.type_animal} {item.name}"

        return f"Самый большой вес {max_weight} кг имеет {heavy}"

    def give_milk(self):
        for item in self.farm:
            item.milk -= 1
        return f'{item.milk} литров у - {item.name} , {horns.milk} литров у - {horns.name} , {manka.milk} литров у - {manka.name}'

    def eat(self):
        for item in self.farm:
            item.weight += 1
        return f'Вы покормили животных'


horns = Goats('Рога', 88 , "беее", 10)
hooves = Goats('Копыта', 89, "беее", 10)
manka = Cow('Манька', 260, "мууу", 10)
koko = Hens('Ко-ко', 1, "кококо", 10)
kukareku = Hens('Кукареку', 3, "кококо", 10)
mallard = Ducks('Кряква', 6, "кря", 10)
baa_lamb = Sheep('Барашек', 90, "меее", 10)
curly = Sheep('Кудрявый', 101, "меее", 10)
gray = Geese('Серый', 4, "гага", 10)
white = Geese('Белый', 7, "гага", 10)

my_farm = {horns, baa_lamb, koko, hooves, mallard, curly, kukareku, manka, gray, white}

all_sound = {horns.sound, baa_lamb.sound, koko.sound, hooves.sound, mallard.sound, curly.sound, kukareku.sound, manka.sound, gray.sound}

milk_giv = {horns, hooves, manka}


mil_far = Far(milk_giv)
finish_farmer = Far(my_farm)
print(finish_farmer.get_heavy())
print(all_sound)
print(mil_far.give_milk())
print(finish_farmer.eat())
print(gray.weight)
