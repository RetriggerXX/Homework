#Task 1
number = str(243)
if number[-1] == "3":
    print(True)
else:
    print(False)


#Task 2
number_1, number_2, number_3 = map(int, input().split())
if number_1 < 0 or number_2 < 0 or number_3 < 0:
    print(True)
else:
    print(False)


#Task 3
number_1, number_2 = map(int, input().split())
if number_1 % 2 == 0 and number_2 % 2 == 0:
    print(True)
elif number_1 % 2 == 1 and number_2 % 2 == 1:
    print(True)
else:
    print(False)


#Task 4
side_a = 5
side_b = 4
side_c = 3
if side_a == side_b == side_c:
    print("equilateral")
elif (side_a == side_b) or (side_a == side_c) or (side_c == side_b):
    print("isosceles")
else:
    print("scalene")


#Task 5
number_1 = 1
number_2 = 2
number_3 = 3
counter = 0
if number_1 % 2 == 0:
    counter += 1
if number_2 % 2 == 0:
    counter += 1
if number_3 % 2 == 0:
    counter += 1
print(counter)


#Task 6
number = str(23)
if int(number[0])+int(number[1]) > 9:
    print(True)
else:
    print(False)


#Task 7
number = str(1111)
if number[0] == number[1] == number[2] == number[3]:
    print(True)
else:
    print(False)


#Task 8
year = 2900
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Високосный")
else:
    print("Не высокосный")


#Task 9
for number in range(20):
    print(10)


#Task 10
start = 5
stop = 10
for number in range(start, stop):
    print(number)


#Task 11
for number in range(100,-101,-1):
    print(number)


#Task 12
counter = 0
for number in range(100, 501):
    counter += number
print(counter)


#Task 13
counter = 1
for number in range(5, 21):
    counter *= number
print(counter)


#Task 14
number = 5
counter = 1
for factorial in range(1,number+1):
    counter *= factorial
print(counter)


#Task 15
n = int(input("Введите n<=1000: "))

for counter in range(1, n+1):

    if counter > 9 :
        last_number = counter % 10
        if counter < 100:
            middle_number = counter // 10         # Узнаем последнее число и число десятков

        else:
            middle_number = ( counter % 100) // 10

        full_number = last_number + middle_number * 10

    else:

        if counter == 1:
            print(f"На лугу {counter} корова")
            continue

        elif counter == 2 or counter == 3 or counter == 4:
            print(f"На лугу {counter} коровы")               # Выводим ответ в числах от 1 до 9
            continue

        else:
            print(f"На лугу {counter} коров")
            continue

    if middle_number == 0:

        if last_number == 1:
            print(f"На лугу {counter} корова")

        elif last_number == 2 or last_number == 3 or last_number == 4:    # Выводим ответ в числах от 1 до 9 в
            print(f"На лугу {counter} коровы")                            # двохзначных и трёхзначных числах

        else:
            print(f"На лугу {counter} коров")

    elif  ((full_number < 20 and full_number > 9) or
        last_number == 0 or
        last_number == 5 or
        last_number == 6 or                                        # Выводим ответ в числах от 10 до 19 и
        last_number == 7 or                                        # которые заканчиваються на 0, 5, 6, 7, 8, 9
        last_number == 8 or
        last_number == 9 ):
        print(f"На лугу {counter} коров")

    elif last_number == 1 :                                        # Выводим ответ в числах которые
        print(f"На лугу {counter} корова")                         # заканчиваються на 1

    else:                                                          # Выводим ответ в числах которые
        print(f"На лугу {counter} коровы")                         # заканчиваються на 2, 3, 4


#Task 16
number = 8
fibo_number = 0
temp_1 = 1
temp_2 = 1
if number == 1:
    print("1")                    # проверки на вероятную ошибку
elif number == 2:
    print('1 1')
else:
    for counter in range(number-2):
        if counter == 0:
                print("1 1",end=" ")
        fibo_number = temp_1 + temp_2
        if counter % 2 == 0:             # Программа расчёт числа фибоначи
            temp_1 = fibo_number
        else:
            temp_2 = fibo_number
        print(fibo_number, end=" ")
print("") # для противодействие end=" "


#Task 17
x1=1
y1=4
x2=5
y2=6

# a)
if ( (x1+y1)%2 == 0 and (x2+y2)%2 == 0 ) or ( (x1+y1)%2 == 1 and (x2+y2)%2 == 1 ):
    print("Поля одного цвета")
else:
    print("Поля не одного цвета")

# b)
if abs(y1-y2) == abs(x1-x2) or x1 == x2 or y1 == y2 :
    print("Queen threatens")
else:
    print("Queen doesn't threatens")

# c)
if ((abs(x2 - x1) == 2 and abs(y1 - y2) == 1 ) or
    (abs(x2 - x1) == 1 and abs(y1 - y2) == 2 )):  # Проверка на угрозу коня на слона
    if abs(y1 - y2) == abs(x1 - x2):
        print("Фигуры угрожают друг другу")

    else:
        print("Только конь угрожает слону")

else:
    if abs(y1 - y2) == abs(x1 - x2):              # Проверка на угрозу слона на коня
        print("Только слон угрожает коню")

    else:
        print("Фигуры не угрожают друг другу ")


