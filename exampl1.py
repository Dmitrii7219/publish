per_cent = {"ТКБ":5.6, "СКБ":5.9, "ВТБ":4.28, "СБЕР":4.0}
money = float(input('Введите сумму вклада  '))
d_tkb = money*per_cent["ТКБ"]
d_skb = money*per_cent.get("СКБ")
d_vtb = money*per_cent.get("ВТБ")
d_sbr = money*per_cent.get("СБЕР")
deposit = [d_tkb, d_skb, d_vtb, d_sbr]
print(deposit)
print('Максимальная сумма, которую вы можете заработать —', max(deposit))
