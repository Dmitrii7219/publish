s = 0.0
n = int(input("Введите количество билетов  "))
for i in range(n):
    age = int(input("Ведите возраст каждого участника  "))
    if age >= 25:
        s = s + 1390.0
    elif 18 <= age < 25:
        s = s + 990.0
    else: s = s + 0.0

if n > 3:
    s = s + 0.1*s
print("Стоимость билетов  ", s)
