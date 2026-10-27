# 10. Processamento de Folha de Pagamento Você foi contratado para criar um sistema de 
# folha de pagamento de uma pequena empresa. O programa deve ler o salário bruto de 
# diversos funcionários (pare o cadastro quando for digitado o salário 0). Para cada 
# funcionário, o sistema deve calcular dois descontos utilizando duas funções distintas: 
# 2. 000, 10%𝑠𝑒𝑓𝑜𝑟𝑎𝑡é𝑅
# ● calcular_inss(salario_bruto): Retorna 8% de desconto se o salário for até R
# 4.000, e um teto fixo de R$ 500 para salários superiores. 
# ● calcular_irrf(salario_base): O salário base é o salário bruto menos o INSS. A 
# função deve isentar quem ganha até R 
# 2. 500. 𝑄𝑢𝑒𝑚𝑔𝑎𝑛ℎ𝑎𝑎𝑐𝑖𝑚𝑎𝑑𝑖𝑠𝑠𝑜𝑎𝑡é𝑅
# 15% sobre o valor que ultrapassar R 
# 2. 500. 𝐴𝑐𝑖𝑚𝑎𝑑𝑒𝑅
# 5.000 paga 
# 5.000, paga 27,5% sobre o valor 
# que ultrapassar R$ 2.500. 
# Durante o laço de repetição, o programa deve exibir o salário líquido de cada funcionário 
# analisado. Ao encerrar o laço, exiba o total acumulado que a empresa pagará de salários 
# líquidos, o valor total arrecadado de impostos (INSS + IRRF) e o maior salário líquido pago na 
# empresa. 


def calcular_inss(salario_bruto):
    if salario_bruto <= 4000:
        return salario_bruto * 0.08
    else:
        return 500.00


def calcular_irrf(salario_base):
    if salario_base <= 2500:
        return 0.0
    elif salario_base <= 5000:
        return (salario_base - 2500) * 0.15
    else:
        return (salario_base - 2500) * 0.275


# Programa principal
total_salarios_liquidos = 0.0
total_impostos = 0.0
maior_salario_liquido = 0.0
quantidade_funcionarios = 0

while True:
    salario_bruto = float(input("Digite o salário bruto do funcionário (0 para encerrar): R$ "))

    if salario_bruto == 0:
        break

    if salario_bruto < 0:
        print("Salário inválido! Digite um valor positivo.")
        continue

    inss = calcular_inss(salario_bruto)
    salario_base = salario_bruto - inss
    irrf = calcular_irrf(salario_base)

    salario_liquido = salario_bruto - inss - irrf

    total_salarios_liquidos += salario_liquido
    total_impostos += inss + irrf
    quantidade_funcionarios += 1

    if salario_liquido > maior_salario_liquido:
        maior_salario_liquido = salario_liquido

    print(f"INSS: R$ {inss:.2f}")
    print(f"IRRF: R$ {irrf:.2f}")
    print(f"Salário líquido: R$ {salario_liquido:.2f}")
    print("-" * 35)

print("\n===== RELATÓRIO DA FOLHA DE PAGAMENTO =====")
print(f"Funcionários processados: {quantidade_funcionarios}")
print(f"Total de salários líquidos: R$ {total_salarios_liquidos:.2f}")
print(f"Total de impostos arrecadados: R$ {total_impostos:.2f}")
print(f"Maior salário líquido: R$ {maior_salario_liquido:.2f}")