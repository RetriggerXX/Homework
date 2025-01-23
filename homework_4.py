#Task 1
def min_of_list_numbers (*args: int) -> int:
    lst = args
    return min(lst)


print(min_of_list_numbers(1, 2))


#Task 2
print(min_of_list_numbers(1, -2, 4, 8))



#Task 3
def distance_calculator (x1: int, y1: int, x2: int, y2: int) -> int:
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


print(distance_calculator(1,1,4,5))



#Tasl 4
def is_simple (num: int) -> bool:
        if num == 2:
            return True
        elif num <= 1 or num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True


print(is_simple(17))



#Task 5
def fibo_number (num: int) -> int or str:
    if num <= 0:
        return "Input value <= 0"
    a1 = 1
    a2 = 1
    for i in range(num-2):
        if i % 2 == 0:
            a1 += a2
        else:
            a2 += a1
    else:
        return max(a1,a2)


print(fibo_number(4))



#Task 6
def closest_mod_5 (number: int) -> int:
        if number % 5 == 0:
            return number
        elif (number+1) % 5 == 0:
            return number+1
        elif (number+2) % 5 == 0:
            return number+2
        elif (number+3) % 5 == 0:
            return number+3
        else:
            return number+4



print(closest_mod_5(6))


#Task 7
def modify_list(lst: list):
    temp = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst[i] = lst[i] // 2
        else:
            temp.append(lst[i])
    for i in range(len(temp)):
        lst.remove(temp[-i])



iron = [1,3,2,4,5,6,7,8,9, 22]
modify_list(iron)
print(iron)


#Task 8
def check_variable(*args: str):
    lst_deny = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
    lst_nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while True:
        temp = True
        string =input('Введите строку: ')
        if string == "Поработали, и хватит":
            return
        for i in range(10):
            if (lst_deny[i] in string) or lst_nums[i] == string[0]:
                print("Нельзя использовать")
                temp = False
        if temp == True:
            print("Можно использовать")




check_variable()





