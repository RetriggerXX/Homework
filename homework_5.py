#Task 1
print([x for x in range(10,100) if x % 2 == 1])


#Task 2
print([x**2 for x in range(1, 11)])


#Task 3
print([x for x in range(100,1000) if x % 3 ==0 and x % 5 == 0])


#Task 4
range_from, range_to, exponentiation = map(int, (input().split()))
lst = ([(x ** exponentiation) for x in range(range_from, range_to)])
for char in lst:
    print(char, end=' ')


#Task 5
print(list(filter(lambda x: "0" in str(x), [1,2,3,4,5,6,7,8,9,10,11,12,13])))


#Task 6
lst = ["Hello", "woaaaaaarld", "a", "withaar", "in", "wawdd", "eayrua", "adsda"]
print(list(filter(lambda x: x.count("a") >= 2, lst)))


#Task 7
lst = ["Hello", "woaaaaaarld", "a", "withaar", "in", "wawdd", "eayrua", "adsda"]
print(list(map(lambda x: x.upper(), lst)))


#Task 8
deny = "1234567890"
lst = ["Hel123lo", "woaaaaaa44rld", "a", "withaar", "in", "w12312300aw878dd", "eayrua", "adsda"]
print(list(map(lambda s: ''.join(c for c in s if c not in deny), lst)))


#Task 9
lst =list(map(int, input().split()))
temp = []
for i in range(len(lst)):
    if (not lst[i] in temp) and lst.count(lst[i]) >= 2:
        print(lst[i], end =' ')
        temp.append(lst[i])
print()


#Task 10
def is_prime(num: int) -> bool:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
print(list(filter(is_prime, range(2,100))))


#Task 11
lst = [7, 4, 1]
def zero_list(lst: list) -> list:
    lens = len(lst)
    index = 0
    while index != lens-1:
        if index < lens :
            if lst[index] > 0 and lst[index + 1] > 0:
               lst.insert(index+1, 0)
               lens += 1
        index += 1
    return lst

print(zero_list(lst))


#Task 12
def sum_neighbors_cyclic(lst: list) -> list:
    new_lst = []
    if len(lst) == 1:
        return lst
    else:
        for i in range(len(lst)):
            if i+1 != len(lst):
                new_lst.append(lst[i-1]+lst[i+1])
            else:
                new_lst.append(lst[i-1]+lst[0])
    return new_lst

lst = list(map(int, input("Введите список чисел ").split()))
for char in sum_neighbors_cyclic(lst):
    print(char, end=' ')

