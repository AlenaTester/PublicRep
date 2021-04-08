tickets = int(input("Введите количество билетов:\n"))
result = 0
count = 0 #счетчик количества выполненных регистраций билетов
for i in range(tickets):
    age = int(input("Введите возраст посетителя:\n"))
    if 0 <= age < 18:
        print("Бесплатный вход")
        result += 0
        count += 1
    elif 18 <= age < 25:
        print("Стоимость билета: 990 руб.")
        result += 990
        count += 1
    elif 25 <= age < 150:
        print("Стоимость билета: 1390 руб.")
        result += 1390
        count += 1
    else:
        print("Введите возраст от 0 до 150 лет. Например: 25 ")
print(f'Общая стоимость {count} билетов: {result} руб.')
if tickets > 3 and count > 3:
    result = result - result * 0.1
    print(f'Общая стоимость {count} билетов с учетом скидки: {result} руб.')