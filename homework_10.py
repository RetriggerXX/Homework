import json

#Task 1

class RangeSquared:

    def __iter__(self):
        return self

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __next__(self):
        if self.start != self.end:
            self.start += 1
            return (self.start - 1) ** 2
        else:
            raise StopIteration


iter1 = RangeSquared(1, 10)
for i in iter1:
    print(i)



#Task 2
def factorial(number: int):
    sum = 1
    for i in range(1,number+1):
        sum *= i
    return sum
n = 9
start = 0
factorial_gen = (factorial(i) for i in range(n+1))
for i in factorial_gen:
    print(i, end=" ")


#Task 3

def read_file_lines(filename, other_filename = "answers.txt"):
    with open(filename, 'r', encoding='utf-8') as file, open(other_filename, 'r', encoding='utf-8') as file2:
        while True:
            line = file.readline()
            line2 = file2.readline()
            if not line and not line2:
                break
            yield line.strip(), line2.strip()

a = read_file_lines("questions.txt")
for _ in range(10):
    print(a.__next__())

#Task 4
def calculate_complex_formula(a, b, c, d, e, f, g, h):
    if a > 0 and g < h:
        return (b * c) + (f * (g + h))
    elif a > 0 and g >= h:
        return (b * c) - ((d - f) / g)
    elif a <= 0 and g < h:
        return -(d / e) + (f * (g + h))
    else:
        return -(d / e) - ((d - f) / g)

print(calculate_complex_formula(1,2,3,4,5,6,7,8))


#Task 5
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Привет, {self.name}!")

    def can_access_adult_site(self):
        if self.age >= 18:
            print(f"Добро пожаловать на сайт для взрослых.")
        else:
            print(f"Добро пожаловать на детский сайт.")

user1 = User("Алекс", 25)
user1.greet()
user1.can_access_adult_site()

user2 = User("Лиза", 12)
user2.greet()
user2.can_access_adult_site()

#Task 6
class CachedFibonacci:

    def __iter__(self):
        return self

    def __init__(self, num: int):

        self.my_num = num
        self.counter = 1
        try:
            with open("fibo.json", 'r') as file:
                self.my_dict = json.load(file)
        except Exception:
            self.my_dict = {"1": 1, "2": 1}

        if num < 0:
            raise ValueError

    def __next__(self):

        if self.counter > self.my_num:
            raise StopIteration

        elif str(self.counter) in self.my_dict:
            result = f"{self.my_dict[str(self.counter)]} from cache"

        else:
            result = self.my_dict[str(self.counter - 1)] + self.my_dict[str(self.counter - 2)]
            self.my_dict[str(self.counter)] = result


        self.counter += 1
        with open('fibo.json', 'w') as file:
            json.dump(self.my_dict, file)
        return result


fibo = CachedFibonacci(24)
for i in fibo:
    print(i)


#Task 7
def check(lst, number) -> bool:
    for divisor in lst:
        if number % divisor == 0:
            return False
    return True

def prime_numbers():
    lst = []
    my_num = 2
    while True:
        if check(lst, my_num):
            lst.append(my_num)
            yield my_num
            my_num +=1
        else:
            my_num += 1


a = prime_numbers()
for _ in range(10):
    print(a.__next__())


#Task 8
class TaskQueue:

    def __iter__(self):
         return self

    def __init__(self, tuple: tuple):
        self.counter = 0
        self.my_tuple = [(tuple[i], tuple[i+1]) for i in range(0, len(tuple), 2)]

        self.my_sorted_tuple = sorted(self.my_tuple, key=lambda x: x[1])
        print(self.counter, len(self.my_sorted_tuple))

    def __next__(self):
        self.counter += 1
        if self.counter-1 < len(self.my_sorted_tuple):
            return self.my_sorted_tuple[self.counter - 1]
        else:
            raise StopIteration


a = TaskQueue(('Задача 2', 4, 'Задача 3', 2, 'Задача 1', 3))
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())