
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