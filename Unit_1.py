salary = int(input("Введите заработную плату в месяц: "))
percent_mortgage = int(input("Введите сколько процентов уходит на ипотеку: "))
percent_life = int(input("Введите сколько роцентов уходит на жизнь: "))
prize = int(input("Введите количество процентов в год: "))

embezzlement_mortgage = salary * percent_mortgage / 100 * 12
accomulation = salary * (1 - (percent_life / 100) - (percent_mortgage / 100)) * 12 + salary * prize * 0.5
print("Расчеты")
print(embezzlement_mortgage)
print(accomulation)