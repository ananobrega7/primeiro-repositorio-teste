# 1. Calculadora de Frete de E-commerce Uma loja virtual precisa de um sistema para 
# calcular o valor do frete. Crie uma função que receba a distância em quilômetros e o tipo de 
# cliente ("Padrão" ou "VIP"). A regra é: R
# 15,00. 
# 0, 50𝑝𝑜𝑟𝑘𝑚𝑟𝑜𝑑𝑎𝑑𝑜.𝑆𝑒𝑎𝑑𝑖𝑠𝑡â𝑛𝑐𝑖𝑎𝑓𝑜𝑟𝑚𝑎𝑖𝑜𝑟𝑞𝑢𝑒100𝑘𝑚,ℎá𝑢𝑚𝑎𝑡𝑎𝑥𝑎𝑓𝑖𝑥𝑎𝑎𝑑𝑖𝑐𝑖𝑜𝑛𝑎𝑙𝑑𝑒𝑅
# Clientes VIP recebem 20% de desconto no valor final do frete. Peça para o usuário inserir os 
# dados e exiba o resultado utilizando a função criada. 


def calcular_frete(distancia, tipo_cliente):
    frete = distancia * 0.50

    if distancia > 100:
        frete += 15.00

    if tipo_cliente == "VIP":
        frete *= 0.80  

    return frete

distancia = float(input("Digite a distância em km: "))
tipo_cliente = input("Digite o tipo de cliente (Padrão ou VIP): ")

valor_frete = calcular_frete(distancia, tipo_cliente)

print(f"Valor do frete: R$ {valor_frete:.2f}")



