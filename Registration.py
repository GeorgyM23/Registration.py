name = 'Goha'
surname = 'Michaliants'
age = '16'

tru = 1
while tru <= 5:
    name1 = input("Введите имя: ")
    surname1 = input("Введите фамилию: ")
    age1 = input("Введите возраст: ")
    if name == name1 and surname == surname1 and age == age1:
        print('Успешно прошли регистрацию')
        break
    else:
        print("Вы ввели что-то не так")
        tru += 1
        continue
