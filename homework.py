# Task 1
print(17 / 2 * 3 + 2)
print(2 + 17 / 2 * 3)
print(19 % 4 + 15 / 2 * 3)
print(15 + 6 - 10 * 4)
print(17 / 2 % 2 * 3 ** 3)


# Task 2
print(17 / 2 * (3 + 2))
print((2 + 17) / 2 * 3)
print(19 % (4 + 15) / 2 * 3)
print((15 + 6 - 10) * 4)
print(17 / 2 % (2 * 3 ** 3))


#Task 3
money = 11
price = 1.5
quantity = 3
print(money-(price*quantity))


#Task 4
apple_anna = 2
apple_paul = 5
print(f'Общее количество яблок Пола и Анны - {apple_anna+apple_paul}')


#Task 5
days = 5
print(f'{days} суток = {days * 24} часов = {days * 1440} минут = {days * 86400} секунд')


#Task 6
days = 182
print(days // 7)


#Task 7
side_1,side_2 = map(int, input("Укажите размеры сторон прямоугольника через пробел: ").split())
print(f'Можно отрезать {(side_1 // 30) * (side_2 // 30)} квадратов')


#Task 8
seconds = 4000
print(f'{seconds // 3600} час')
print(f'{(seconds % 3600) // 60} минут')
print(f'{seconds % 60} секунд')


#Task 9
cash = 361
print(cash // 100 , "купюры по 100 рублей")
print((cash % 100) // 50 , "купюры по 50 рублей")
print((cash % 50) // 10 , "купюры по 10 рублей")
print((cash % 10) // 1 , "купюры по 1 рублей")


#Task 10
height = 5
up = 3
down = 2
srinted_height = height - up  # высота при которой улитка не будет спускаться на след. день
srinted_height = (((srinted_height * srinted_height) ** (1 / 2) + srinted_height) / 2) #проверка если height < up
print("на",int(srinted_height // (up-down)) + 1 ,
"день улитка доползет до вершины") # рассчитываем сколько нужно дней для достижение
                                    # srinted_height и добавляем 1 день на финальный рывок


#Task 11
length = 56
speed = 60
hours = 1
minutes = 20
time = hours + (minutes / 60) # переводим в удобное для формул время
distance = time * speed # рассчитываем какую дистанцию проедет байкер
print(distance % length) # рассчитываем в какой точке остановиться байкер
