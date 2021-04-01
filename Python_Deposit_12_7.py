money = int(input("Введите сумму вклада (руб.): "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
per_cent_values = list(per_cent.values())
deposit = list(map(lambda x: money * x * 0.01, per_cent_values))
deposit = list(map(int, deposit))
print("deposit = ", deposit)
print("Максимальная сумма, которую вы можете заработать — ", max(deposit))
