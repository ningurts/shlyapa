salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

total_spend = 0  # Общие расходы за все месяцы

for month in range(months):
    total_spend += spend - salary
    spend *= (1 + increase)

money_capital = total_spend  # Необходимая подушка безопасности

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
 