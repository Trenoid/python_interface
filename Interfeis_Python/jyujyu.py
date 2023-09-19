zarplata_1 = int(input("Введите зарплату"))
kolvo_1 = int(input("Введите количество выдач зарплаты"))

balance = 0

for i in range(kolvo_1):
    balance = balance + zarplata_1

print(balance)