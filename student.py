class Student:
    def __init__(self, name = "Ivan", age = "18", group_number = "10A"):
        self. name = name
        self. age = age
        self. groupnumber = group_number
    def get_name(self):
        return f"имя - {self.name}"
    def get_age(self):
        return f"возраст - {self.age}"
    def get_group_number(self):
        return f"номер группы - {self.groupnumber}"
    def set_name_age(self, name, age):
        self. name = name
        self. age = age
        return f"имя - {self.name}, возраст - {self.age}"
    def set_group_number(self, group_number):
        self. groupNumber = group_number
        return f"группа -{self.groupNumber}"


Vlad = Student('Влад',18,"11A")

Dasha = Student("даша", 17, "10B")
Egor = Student()
Anton = Student()
Sonya = Student("соня", 16, "9Б")
print(f'{Vlad.get_name()}, {Vlad.get_age()}, {Vlad.get_group_number()}')
print(f'{Dasha.get_name()}, {Dasha.get_age()}, {Dasha.get_group_number()}')
print(f'{Egor.set_name_age("Егор", 19)}, {Egor.set_group_number("3ИСП")}')
print(f'{Anton.set_name_age("Антон", 18)}, {Anton.set_group_number("2ИСП")}')
print(f'{Sonya.get_name()}, {Sonya.get_age()}, {Sonya.get_group_number()}')
