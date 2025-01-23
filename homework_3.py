#Task 1
number = 15
counter = 1
while True:
    if (counter ** 2) < number:
        print(counter ** 2 , end=" ")
    else:
        print(" ")
        break
    counter += 1



#Task 2
number = 6723
while True:
    if number // 10 == 0:
        print(number)
        break
    else:
        number //= 10



#Task 3
number = 856
minimal = number % 10
while ((number // 10) % 10) != 0:
    number //= 10
    if minimal > (number % 10):
        minimal = number % 10
print(minimal)



#Task 4
stroka = "Hello World!"
print(stroka[2])                                          #1
print(stroka[-2])                                         #2
print(stroka[0],stroka[1],stroka[2],stroka[3],stroka[4])  #3
print(stroka[:-2])                                        #4
for _ in range(0,len(stroka),2): print(stroka[_], end="") #5
print("")
for _ in range(1,len(stroka),2): print(stroka[_], end="")   #6
print("")
for _ in range(len(stroka) - 1,-1,-1): print(stroka[_], end="") #7
print("")
for _ in range(len(stroka) - 1,-1,-2): print(stroka[_], end="") #8
print("")
print(len(stroka))                                              #9



#Task 5
stroka ="Hello world"
word_1 = ""
word_2 = ""
space = stroka.index(" ")
for i in range(space, len(stroka)):
    word_2 += stroka[i]
for i in range(space):
    word_1 += stroka[i]
stroka_reversed = word_2 +" " + word_1
print(stroka_reversed)



#Task 6
stroka = "топрот"
stroka = stroka.lower()
for i in range((len(stroka) // 2)):
    if stroka[i] == stroka[-(i + 1)]:
        continue
    else:
        print("Не палиндром")
        break
else:
    print("Палиндром")



#Task 7
stroka = "qwefrtfy"
if "f" in stroka:
    print(stroka.index("f"))
    if stroka.count('f', stroka.index("f") + 1, len(stroka)):
        print(stroka.count('f'))



#Task 8
list_1 = [5, 8, 12, 34, 19 ,21 ,36 , 33]
list_2 = [1, 2, 3, 5, 6, 7, 8, 9]
list_1.sort()
for i in range(len(list_1)):
    if list_1[i] not in list_2:
        print(list_1[i])
        break



#Task 9
k= 8
list_1 = [10,3,4,8,2,0,7,3]
counter = 0
for first_number in range(k-1):
    second_number = first_number + 1
    if list_1[first_number] > list_1[second_number]:
        counter += 1
print(counter)



#Task 10
stroka = input("Введите строку: ")
lst = []
new_stroka = ()
for i in range(len(stroka)):
    if not (stroka[i] in lst):
        lst.append(stroka[i])
print(''.join(lst))


#Task 11
stroka = "я отдам тебе 30к через 18 дней, если подождешь 20 дней отдам 40к"
lst = []
num = ''
for i in range(len(stroka)):
    if stroka[i].isdigit():
        num = num + stroka[i]
    elif num == '':
        continue
    else:
        lst.append(num)
        num = ''
print(max(lst))



#Task 12
stroka = input("Введите строку: ")
new_stroka = ""
for i in range(len(stroka)):
    temp=stroka[0]
    stroka = stroka[:0] + stroka[0 + 1:]
    if not(temp in stroka):
        new_stroka += temp
print(new_stroka)


#Task 13
lst = [15,13,22,14,89,12,104,50004]
new_lst = []
for i in range(len(lst)):
    new_lst.append(lst[i])
    temp = str(lst[i])
    new_lst.append(int(temp[::-1]))
print(new_lst)