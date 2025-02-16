import math

#Task 1
class Nums:
    def __init__(self, num1 :int, num2: int):
        self.num1 = num1
        self.num2 = num2

    def summa(self):
        return (self.num1 + self.num2)  #сумма чисел

    def max(self):
        return max(self.num1, self.num2) #вывод максимального среди чисел


#Task 2
class Counter:
    def __init__(self, num: int):
        self.num = num

    def increase(self):
        if self.num < 9:
            self.num += 1 #добавляет +1 к счетчику
        else:
            raise ValueError('Значение счетчика больше 9')

    def decrease(self):
        if self.num > 0:
            self.num -= 1 #отнимает -1 от счетчика
        else:
            raise ValueError('Значение счетчика меньше 0')

    @property
    def value(self):    #выводит значение счетчика
        return self.num


counter = Counter(8)
counter.increase()
counter.decrease()
counter.decrease()
print(counter.value)


#Task 3
class Shop:
    def __init__(self):
        self.products = {}

    def add_product(self, product_name:str, price: float): #добавляет продукт и его цену
        self.products[product_name] = price

    def del_product(self,product_name:str):
        try:
            del self.products[product_name]         #удаляет продукт если он есть
            print('Продукт удален')
        except Exception:
            print("Нету продукта")

    def find_product(self,product_name:str):
        try:
            print(f"{product_name} стоит {self.products[product_name]} баксов")
        except Exception:
            print("Нету такого")        #ищет продукт в магазине

    def assortment(self) :
        print(self.products)        #выводит ассортимент магазина


prostore = Shop()
prostore.add_product('сметана', 10.25)
prostore.add_product('туалетная бумага', 14.65)
prostore.add_product('молоко', 12.95)
prostore.add_product('сыр', 4.6)
prostore.add_product('колбаса', 61)
prostore.add_product('йогурт', 45.5)
prostore.del_product('сметана')
prostore.assortment()


#Task 4
class MoneyBox:
    def __init__(self,capacity):
        self.capacity = capacity        #инициализация переменных копилки
        self.money_inside = 0

    def can_add(self, v: int) -> bool:
        if (self.capacity - self.money_inside) > v:     #функция проверка вместимости копилки
            return True
        else:
            return False

    def add(self,v):
        self.money_inside += v      #функция добавление в копилку

mybox = MoneyBox(20)
mybox.add(15)
print(mybox.can_add(6))

#Task 5
class Fraction:
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator

    @property
    def info(self):
        return f"{self.numerator/self.denominator}"

    def adding_fractions(self, numerator2, denominator2):
        new_numerator = self.numerator * denominator2 + numerator2 * self.denominator
        new_denominator = self.denominator * denominator2
        gcd = math.gcd(new_denominator, new_numerator)
        result = f"{new_numerator//gcd}/{new_denominator//gcd}"
        if new_denominator//gcd == 1:
            return new_numerator//gcd
        else:
            return result
    @property
    def reducing_fractions(self):
        gcd = math.gcd(self.denominator, self.numerator)
        result = f"{self.numerator // gcd}/{self.denominator // gcd}"
        if self.denominator // gcd == 1:
            return self.numerator // gcd
        else:
            return result


my_float = Fraction(3,23)
print(my_float.adding_fractions(43,23))
my_float = Fraction(3,21)
print(my_float.reducing_fractions)

#Task 6

class Abiturient:
    def __init__(self, student_name):
        self.student_name = student_name
        self.my_rates = []

    def register_to_facultet(self, facultet):
        facultet.register(self)

    def go_to_exam(self, exam):
        exam.add_student(self)

    def add_rate(self, mark):
        self.my_rates.append(mark)

    def avarage_marks(self):
        if len(self.my_rates) == 0:
            return 0
        return sum(self.my_rates) / len(self.my_rates)

class Facultet:
    def __init__(self, facultet_name, min_score_to_enter):
        self.facultet_name = facultet_name
        self.min_score_to_enter = min_score_to_enter
        self.list_of_registred_students = []

    def register(self, student):
        self.list_of_registred_students.append(student)

    def admit_students(self):
        admitted_students = [student for student in self.list_of_registred_students if student.avarage_marks() >= self.min_score_to_enter]
        return admitted_students

class Exam:
    def __init__(self):
        self.list_of_students_who_was_on_exam = []

    def add_student(self, student):
        self.list_of_students_who_was_on_exam.append(student)

    def check_student(self, student):
        return student in self.list_of_students_who_was_on_exam

class Teacher:
    def rate_student(self, exam, student, mark):
        if exam.check_student(student):
            student.add_rate(mark)

class System:
    def process_admissions(self, facultet):
        admitted_students = facultet.admit_students()
        for student in admitted_students:
            print(student.student_name, "зачислен")

student = Abiturient("Ivan")
facultet = Facultet("Computer Science", 80)
exam = Exam()
teacher = Teacher()
system = System()
student.register_to_facultet(facultet)
student.go_to_exam(exam)
teacher.rate_student(exam, student, 85)
teacher.rate_student(exam, student, 90)
system.process_admissions(facultet)



