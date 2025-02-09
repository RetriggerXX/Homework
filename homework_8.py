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


