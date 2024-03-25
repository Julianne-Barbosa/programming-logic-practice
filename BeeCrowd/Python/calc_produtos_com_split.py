product1 = input().split(" ")
product2 = input().split(" ")
code1, qtd1, price1 = product1
code2, qtd2, price2 = product2

total = (int(qtd1)*float(price1)) + (int(qtd2)*float(price2))

print(f"VALOR A PAGAR: R$ {total:.2f}")