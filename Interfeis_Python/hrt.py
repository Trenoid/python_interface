# Написать калькулятор, дается первое число, затем второе, затем что сделать с этими числами
while 1 == 1:
    pervoe_chislo = int(input("Введите первое число: "))
    vtoroe_chislo = int(input("Введите второе число: "))
    operator = input("Введите оператор: ")

    if operator == "+":
        print("Summa ravna: ", pervoe_chislo + vtoroe_chislo)

    elif operator == "-":
        print("Разность ravna: ", pervoe_chislo - vtoroe_chislo)

    elif operator == "*":
        print("Произведение ravna: ", pervoe_chislo * vtoroe_chislo)

    else: print("Такого оператора не существует")

print(f"пклоп")

