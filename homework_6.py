#Task 1

lst = ["Hello","world","my","name","is","Maksym","im","18","years","old"]
lst.sort(reverse=True, key=lambda x: len(x))
print(lst)


#Task 2
lst = ['aaa',"Hello","world","my","name","is","Maksym","im","18","years","old",'aa']
lst.sort(key=lambda x: x.count('a'))
print(lst)

#Task 3
school = {'class_9a': 12, 'class_9b': 32,'class_9c': 12,
         'class_9d': 32,'class_9e': 12, 'class_9r': 32}
school['class_9a'] = 30
school['class_9f'] = 2
del school['class_9b']
print(sum(school.values()))

#Task 4
contacts = {}
incoming = ""
while True:
    incoming = input("Введите номера: ").split()
    if incoming == ['.']:
        break
    elif len(incoming) == 2:
        value1, value2 = incoming
        contacts[value1] = value2
    else:
        value1 = incoming[0]
        if value1 in contacts:
            print(contacts[value1])
        else:
            print("не найдено")

# #Task 5
def get_element(lst: list, index: int):
    try:
        return lst[index]
    except (IndexError):
        return 'IndexError "Ошибка: индекс вне диапазона"'

print(get_element([1,2,3,4,5,6,7,8,9,10], 11))

#Task 6
def retry_on_exception(retries: int):
    def decorator(func):
        def wrapper(a: int, b: int):
            for x in range(retries):
                try:
                    return func(a, b)
                except ValueError:
                    print(f'ValueError, retrying {retries - x} more times')
            return ValueError("Превышено количество попыток")
        return wrapper
    return decorator

@retry_on_exception(3)
def div(a: int, b: int):
    return float(a), float(b)


print(div("a", 0))

#Task 7
#забуксовал здесь, код впринципе есть, но он написан другими
#пользователями интернета и я его особо не понимаю

#Task 8
stroka = "a A a"
stroka = stroka.lower()
print(stroka)
lst = stroka.split(" ")
temp = []
for i in range(len(lst)):
    if lst[i] not in temp:
        print(lst[i], lst.count(lst[i]))
        temp.append(lst[i])


#Task 9
cache = {}

def cache_result(func):
    def wrapper(a: int):
        if a in cache:
            return cache[a]
        else:
            cache[a] = func(a)
            return cache[a]
    return wrapper

@cache_result
def quadro(a: int):
    return a ** a

print(quadro(2))
print(quadro(2))
print(quadro(2))
print(quadro(1))
print(quadro(3))
print(cache)

