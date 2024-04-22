CREDITO_CARBONO_VALOR = 89.05


def calculo(coeficientes):
    while True:
        try:
            valor_quilometro = (
                float(input('\nDigite a quantidade de quilômetros rodados por um tipo de veículo (Km): '))
            )
            break
        except ValueError:
            print('\nResposta inválida, por favor, digite somente números!')

    print('\nTipos de combustivel: 1- Gasolina; 2 - Diesel; 3 - Eletrico; 4 - Etanol')
    tipo_combustivel = input('\nDigite o tipo de combustível (1/2/3/4): ').strip()
    while tipo_combustivel not in ['1', '2', '3', '4']:
        print('Resposta inválida, digite apenas os números (1/2/3/4).')
        tipo_combustivel = input('Digite o tipo de combustível (1/2/3/4): ').strip()

    while True:
        try:
            unidade = 'Km/kWh' if tipo_combustivel == '3' else 'Km/L'
            valor_consumo_combustivel = float(input(f'\nDigite o consumo do respectivo combustível ({unidade}): '))
            break
        except ValueError:
            print('Resposta inválida, por favor, digite somente números!')

    coeficiente = coeficientes.get(tipo_combustivel)
    quantidade_carbono = (valor_quilometro / valor_consumo_combustivel) * coeficiente

    return quantidade_carbono


def calcular_consumo(coeficientes, ano):
    quantidade_carbono = 0

    print(f'\nAgora, responda com os valores referentes ao {ano} ano da comparação.')
    quantidade_carbono += calculo(coeficientes)

    while True:
        adicionar_mais_consumo = input(f'\nDeseja adicionar mais algum consumo nesse {ano} ano? (S/N) ').strip().lower()
        if adicionar_mais_consumo == 's':
            quantidade_carbono += calculo(coeficientes)
        elif adicionar_mais_consumo == 'n':
            break
        else:
            print('Resposta inválida, responda com S(sim) ou N(não)')

    return quantidade_carbono


def main():
    coeficientes = {
        '1': 0.00407,
        '2': 0.00468,
        '3': 0.00084,
        '4': 0.0022755
    }

    print('************************************************')
    print('*Bem-vindo a calculadora de crédito de carbono!*')
    print('************************************************')

    resposta_boas_vindas = input('\nEstá tudo pronto para realização do cálculo? (S/N) ').strip().lower()

    if resposta_boas_vindas != 's':
        if resposta_boas_vindas != 'n':
            print('Resposta inválida!')
        print('Calculadora encerrada.')
        return

    quantidade_carbono_primeiro_ano = calcular_consumo(coeficientes, "primeiro")
    quantidade_carbono_segundo_ano = calcular_consumo(coeficientes, "segundo")

    diferenca = quantidade_carbono_primeiro_ano - quantidade_carbono_segundo_ano
    valor_em_reais = CREDITO_CARBONO_VALOR * diferenca

    if diferenca > 0:
        print(f'\nParabéns! Você adquiriu {diferenca:0.2f} créditos de carbono.')
        print(f'Com isso, você receberá {valor_em_reais:0.2f} reais na venda desses créditos! ')
    elif diferenca == 0:
        print(f'\nSeu consumo foi igual nos dois anos! Logo, você não adquiriu nenhum crédito de carbono.')
    else:
        diferenca = abs(diferenca)
        print(f'\nInfelizmente, suas emissões aumentaram em {diferenca:.2f}!')
        print(f'Portanto, para compensar o aumento de emissões, '
              f'você deve comprar {diferenca:0.2f} créditos de carbono!')
        print(f'Para isso, você deverá desembolsar {valor_em_reais:0.2f} reais.')


if __name__ == '__main__':
    main()
