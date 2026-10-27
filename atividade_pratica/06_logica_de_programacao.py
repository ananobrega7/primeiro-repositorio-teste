# 6. Sistema de Tarifas de Táxi Crie duas funções distintas: tarifa_diurna(distancia) e 
# tarifa_noturna(distancia). A tarifa diurna cobra R 
# 4, 00𝑑𝑒𝑏𝑎𝑛𝑑𝑒𝑖𝑟𝑎𝑑𝑎𝑚𝑎𝑖𝑠𝑅
# km. A noturna cobra R 
# 6, 00𝑑𝑒𝑏𝑎𝑛𝑑𝑒𝑖𝑟𝑎𝑑𝑎𝑚𝑎𝑖𝑠𝑅
# 2,50 por 
# 3,20 por km. O programa principal deve usar 
# um laço para atender vários passageiros ao longo do turno de um motorista. Para cada 
# passageiro, pergunte se a corrida foi de dia (D) ou de noite (N) e a distância. Chame a função 
# adequada e some o valor para o caixa do motorista. O turno acaba quando a distância 
# informada for negativa. 


def tarifa_diurna(distancia):
    return 4.00 + 2.50 * distancia


def tarifa_noturna(distancia):
    return 6.00 + 3.20 * distancia


# Programa principal
caixa_motorista = 0.0

while True:
    distancia = float(input("Digite a distância da corrida em km (negativa para encerrar): "))

    if distancia < 0:
        break

    periodo = input("A corrida foi de dia (D) ou de noite (N)? ").upper()

    if periodo == "D":
        valor = tarifa_diurna(distancia)
    elif periodo == "N":
        valor = tarifa_noturna(distancia)
    else:
        print("Período inválido! Digite D ou N.")
        continue

    caixa_motorista += valor

    print(f"Valor da corrida: R$ {valor:.2f}")
    print(f"Total acumulado no caixa: R$ {caixa_motorista:.2f}")
    print("-" * 35)

print(f"\nTurno encerrado! Total no caixa: R$ {caixa_motorista:.2f}")