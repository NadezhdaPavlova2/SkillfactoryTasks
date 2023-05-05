count=0
amount_tickets=int(input("Введите количество билетов: "))
for i in range(amount_tickets):
    age_tickets=int(input(f"Введите возраст для билета {i+1}: "))
    if age_tickets < 18:
        count += 0
    elif 18 <= age_tickets <= 25:
        count += 990
    else:
        count += 1390
if amount_tickets > 3:
    count *= 0.9
print("Сумма к оплате: ", count)