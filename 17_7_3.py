money = int(input('Введите сумму: '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
#Другой вариант решения:
#for key in per_cent.keys():
#    deposit.append(int(money * per_cent[key] / 100))
deposit.append(int(money*per_cent['ТКБ']/100))
deposit.append(int(money*per_cent['СКБ']/100))
deposit.append(int(money*per_cent['ВТБ']/100))
deposit.append(int(money*per_cent['СБЕР']/100))
max_deposit = max(deposit)
print(deposit, '\nМаксимальная сумма, которую вы можете заработать: ', max_deposit)

