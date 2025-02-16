from datetime import datetime
import json
import re
from random import randint
import fileinput




#Task 1
class BankAccount:
    def __init__(self, balance:float=0):
        self.__balance = balance
        self.daily_limit = 5000
        self.withdrawals_today = 0
        self.max_withdrawals = 3
        self.last_withdrawals = datetime.strptime("2025-02-13","%Y-%m-%d").date() #свое значение

    def deposit(self, amount: float):

        if datetime.today().date() > self.last_withdrawals:
            self.last_withdrawals = datetime.today().date()
            self.withdrawals_today = 0
            self.daily_limit = 5000

        if self.withdrawals_today == self.max_withdrawals:
            print("Transaction limit for the day has been exceeded, come back tomorrow")

        else:
            self.__balance += amount
            self.withdrawals_today += 1
            print("Transaction successful")


    def withdraw(self, amount: float):

        if datetime.today().date() > self.last_withdrawals:
            self.last_withdrawals = datetime.today().date()
            self.withdrawals_today = 0
            self.daily_limit = 5000

        if self.__balance < amount:
            print('Insufficient funds')

        elif amount > self.daily_limit:
            print(f"The amount to withdraw is too large, your daily limit is {self.daily_limit} for today")

        elif self.withdrawals_today == self.max_withdrawals:
            print("Transaction limit for the day has been exceeded, come back tomorrow")

        else:
            self.__balance -= amount
            self.withdrawals_today += 1
            self.daily_limit -= amount
            print("Transaction successful")


    def get_balance(self):

        print(f"Your balance - {self.__balance}")

bank = BankAccount()
bank.deposit(100000)
bank.withdraw(4000)
bank.withdraw(2000)
bank.withdraw(1000)
bank.withdraw(0)

#Task 2

#в animals.json храниться еда для каждого животного

class Animal:

    def __init__(self, name: str, age: int,):
        self.name = name
        self.age = age
        self.hunger = 100  # 100 - сыт, 0 - голоден
    def make_sound(self):
        return print("Some sound")

    def eat(self,food: str):
        return print(f"{self.name} say 'nah'")



class Lion(Animal):

    def make_sound(self):
        return print("Raaar")

    def hunt(self):
        print(f"{self.name} is hunting.")

    def eat(self,food: str):
        if self.hunger <= 0:           #проверка на сытость животного
            return print(f"{self.name} is dead, it doesn't eat anymore :(")

        with open("animals.json", "r") as fh:    #открываем файл
            animals_food_dict = json.load(fh)

        if food in animals_food_dict["Lion"]:    #проверка подходит ли льву еда
            self.hunger += animals_food_dict["Lion"].get(food)
            if self.hunger >= 100:
                self.hunger = 100
            return print(f"{self.name} happily ate everything")
        else:
            return print(f"{self.name} say 'nah'")

    def hunger_level(self):
        if self.hunger <= 0:
            return print(f"{self.name} is dead :(")
        return print(f"{self.name} is {self.hunger}% hungry")

    def time_travel(self, time_in_hours:int):
        self.hunger -= time_in_hours // 3.36   #коэффициент голода льва за час

class Elephant(Animal):

    def make_sound(self):
        return print("Truuuuu")

    def trumpet(self):
        print(f"{self.name} is trumpeting.")

    def eat(self, food: str):
        if self.hunger <= 0:        #проверка на сытость животного
            return print(f"{self.name} is dead, it doesn't eat anymore :(")

        with open("animals.json", "r") as fh:   #открываем файл
            animals_food_dict = json.load(fh)

        if food in animals_food_dict["Elephant"]:   #проверка подходит ли слону еда
            self.hunger += animals_food_dict["Elephant"].get(food)
            if self.hunger >= 100:
                self.hunger = 100
            return print(f"{self.name} happily ate everything")
        else:
            return print(f"{self.name} say 'nah'")

    def hunger_level(self):
        if self.hunger <= 0:
            return print(f"{self.name} is dead :(")
        return print(f"{self.name} is {self.hunger}% hungry")

    def time_travel(self, time_in_hours:int):
        self.hunger -= time_in_hours // 6.72    #коэффициент голода слона за час

class Penguin(Animal):

    def make_sound(self):
        return print("Waah")

    def swim(self):
        print(f"{self.name} is swimming.")

    def eat(self, food: str):
        if self.hunger <= 0:        #проверка на сытость животного
            return print(f"{self.name} is dead, it doesn't eat anymore :(")

        with open("animals.json", "r") as fh:   #открываем файл
            animals_food_dict = json.load(fh)

        if food in animals_food_dict["Penguin"]:    #проверка подходит ли пингвину еда
            self.hunger += animals_food_dict["Penguin"].get(food)
            if self.hunger >= 100:
                self.hunger = 100
            return print(f"{self.name} happily ate everything")
        else:
            return print(f"{self.name} say 'nah'")

    def hunger_level(self):
        if self.hunger <= 0:
            return print(f"{self.name} is dead :(")
        return print(f"{self.name} is {self.hunger}% hungry")

    def time_travel(self, time_in_hours:int):
        self.hunger -= time_in_hours // 10.8    #коэффициент голода пингвина за час

lion = Lion("lion Barsik", 9)
elephant = Elephant("Elephant Jora",18)
penguin = Penguin("Penguin Lolo", 6)

lst = [lion, elephant, penguin]
for animal in lst:
    animal.time_travel(500)
    animal.hunger_level()
    animal.eat("Octopus")
    animal.hunger_level()


#Task 3

class Temperature:
    def __init__(self, cels: float):
        if cels < -273.15:
            raise ValueError("Недопустимое значение")
        else:
            self.cels = cels

    def celsius(self, cels: float):
        if cels < -273.15:
            raise ValueError("Недопустимое значение")
        else:
            self.cels = cels

    @property
    def fahrenheit(self):
        return (self.cels*9/5) + 32

    @property
    def kelvin(self):
        return self.cels + 273.15

temperatura = Temperature(87)
print(temperatura.fahrenheit)
print(temperatura.kelvin)


#Task 4

class User:

    def __init__(self, name, email):
        self.name = name.lower()
        self._email = email.lower()

        #проверка почты
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$' #патерн почты
        if not re.match(pattern, email):
            raise ValueError("Некорректный email")

        #проверка имени
        try:
            with open('ID.json', 'r') as file:
                logs = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            logs = {}

        if self.name in logs:
            raise NameError("Другой пользователь уже присвоил данное имя")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("logins.txt", "a") as file:                   #записываем в логи данные
            file.write(f"[{timestamp}] NAME: {name} EMAIL: {email}\n")

        if self.name not in logs:
            while True:
                rand = randint(0, 100000)
                if rand not in logs.values():
                    logs[self.name] = rand  # Присваиваем уникальный ID
                    break

            with open('ID.json', 'w') as file:
                json.dump(logs, file)


    def rename(self, new_name):

        with open('ID.json', 'r+') as file:
            logs = json.load(file)
            if new_name in logs:
                raise NameError("Другой пользователь уже присвоил данное имя")
            file.seek(0)
            logs[new_name] = logs.pop(self.name)
            json.dump(logs, file)
            file.truncate()

        for line in fileinput.input('logins.txt', inplace=True):
            # f строка предназначена для предотвращение замены текста с почты
            print(line.replace(f' {self.name} ', f' {new_name} '), end='')

        self.name = new_name



    def log_login(self):
        if self.name == 'admin':
            with open("logins.txt", "r") as file:
                print(file.read())
        else:
            raise PermissionError("Недостаточно прав")


    def info(self):
        return print(self.name, self._email)


admin = User('admin', "admin@gmail.com")
user = User("vova", "vova@asdd.com")
admin.log_login()
user.rename('yarik')
user.info()
admin.info()



with open("ID.json", "w") as _, open("logins.txt", "w") as _:   #очистка логов
    pass


