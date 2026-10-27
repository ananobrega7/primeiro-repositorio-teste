# 5. Simulador de Rendimentos Crie uma função chamada calcular_juros que receba um 
# valor inicial, uma taxa de juros mensal e um número de meses. O programa deve usar um laço 
# de repetição dentro ou fora da função para calcular o crescimento do dinheiro mês a mês, 
# aplicando juros compostos. O programa deve imprimir o saldo ao final de cada mês. Se em 
# algum mês o saldo dobrar em relação ao valor inicial, o laço deve ser interrompido e uma 
# mensagem de "Meta Atingida antecipadamente!" deve ser exibida. 


def calcular_juros(valor_inicial, taxa_mensal, meses):
    saldo = valor_inicial
    mes = 1

    while mes <= meses:
        saldo = saldo * (1 + taxa_mensal / 100)

        print(f"Saldo ao final do mês {mes}: R$ {saldo:.2f}")

        if saldo >= valor_inicial * 2:
            print("Meta Atingida antecipadamente!")
            break

        mes += 1

    return saldo


# Entrada de dados
valor_inicial = float(input("Digite o valor inicial (R$): "))
taxa_mensal = float(input("Digite a taxa de juros mensal (%): "))
meses = int(input("Digite o número de meses: "))

# Executa o simulador
calcular_juros(valor_inicial, taxa_mensal, meses)