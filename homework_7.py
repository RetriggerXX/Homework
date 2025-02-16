
from datetime import datetime, timedelta
import json
import pandas
import re

#Task 1
file = open("input.txt", "w+")
numbers = ["1,2,3,4,5,6,7,8,9,10"]
for i in range(len(numbers)): #добавляет поштучно елементы списка
    file.write(str(numbers[i]))


#Task 2
file.seek(0)
numbers_str = file.read() #читает файл
new_numbers = numbers_str.split(",") #убирает ","
result = list(map(int, new_numbers)) #преобразование каждого елемента в числовой
file2 = open("output.txt", "w+")
file2.write(str(sum(result))) #запись суммы в аутпут файл
file2.seek(0)
print(file2.read())


#Task 3
date_now = pandas.to_datetime('today').normalize() #сегодняшняя дата
with open("shop.txt", "r") as file:
    for line in file:
        words = line.split()
        date_shop = datetime.strptime(words[3], '%d.%m.%Y') #преобразования даты из файла
        time_difference = date_now - date_shop #разница между сегодняшним днем и датой поступления товара
        if time_difference > timedelta(days=30) and (int(words[1])*int(words[2])) >= 1000000:
            print(f"{words[0]} храниться больше месяца и стоимость превышает 1 000 000 р.")

#Task 4
counter = 0
with open("questions.txt", "r", encoding="utf-8") as questions, open('answers.txt', 'r', encoding="utf-8") as answers:
    for _ in range(10):
        answer = answers.readline().strip()     #считывания рядка с вопросом
        question = questions.readline().strip()     #считывания рядка с ответом
        user_answer = input(f"{question} Введите ответ: ")
        if user_answer.lower() == answer.lower():
            counter += 1
print(f"Количество правильных ответов - {counter} ")


#Task 5
my_dict =  {
    11111: ("Andrey", 15),
    00000: ("Sofia", 43),
    12345: ("Petr", 32),
    23456: ("Alexey", 65),
    34567: ("Mike", 12),
    45678: ("John", 22)
}
json_data = json.dumps(my_dict, indent=4) #преобразование в формат json
with open('data.json', 'w') as file:
    file.write(json_data)
with open('data.json', "r") as file:
    data = json.load(file)
print(data)

#Task 6
data_for_csv = pandas.DataFrame(data)
data_for_csv.to_csv('data.csv', index=False)

#Task 7
my_dict = {}
with open('7.txt', 'r') as file:
    for _ in file:
        line = list(file.readline().strip().split(" "))
        for i in range(len(line)):
            if line[i] in my_dict:
                my_dict[line[i]] += 1
            else:
                my_dict[line[i]] = 1

    max_key = max(my_dict, key=my_dict.get)
    print(max_key,my_dict[max_key])

#Task 8
with open('8.txt', 'r') as file:
    lst = re.findall(r'[A-Za-z]|\d+', file.read())
    for i in range(0,len(lst),2):
        print(lst[i]*int(lst[i+1]),end="")