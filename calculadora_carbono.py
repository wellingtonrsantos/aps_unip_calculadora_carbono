CREDITO_CARBONO_VALOR = 168.19

FATOR_EMISSAO = {
    '1': 1.68392,   # Gasolina
    '2': 2.38069,   # Diesel
    '3': 0.00050,   # Eletrico
    '4': 0.01415    # Etanol
}


def calcular_emissao_carbono():
    while True:
        try:
            quilometros_percorridos = (
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

    fator_emissao = FATOR_EMISSAO.get(tipo_combustivel)
    return (quilometros_percorridos / valor_consumo_combustivel) * fator_emissao


def calcular_consumo(ano):
    quantidade_emissao_carbono = 0

    print(f'\nAgora, responda com os valores referentes ao {ano} ano da comparação.')
    quantidade_emissao_carbono += calcular_emissao_carbono()

    while True:
        adicionar_mais_consumo = input(f'\nDeseja adicionar mais algum consumo nesse {ano} ano? (S/N) ').strip().lower()
        if adicionar_mais_consumo == 's':
            quantidade_emissao_carbono += calcular_emissao_carbono()
        elif adicionar_mais_consumo == 'n':
            break
        else:
            print('Resposta inválida, responda com S(sim) ou N(não)')

    return quantidade_emissao_carbono


def main():
    print('************************************************')
    print('*Bem-vindo a calculadora de crédito de carbono!*')
    print('************************************************')

    resposta_boas_vindas = input('\nEstá tudo pronto para realização do cálculo? (S/N) ').strip().lower()

    if resposta_boas_vindas != 's':
        if resposta_boas_vindas != 'n':
            print('Resposta inválida!')
        print('Calculadora encerrada.')
        return

    quantidade_carbono_primeiro_ano = calcular_consumo("primeiro")
    quantidade_carbono_segundo_ano = calcular_consumo("segundo")

    diferenca_anos = quantidade_carbono_primeiro_ano - quantidade_carbono_segundo_ano
    valor_em_reais = CREDITO_CARBONO_VALOR * diferenca_anos

    if diferenca_anos > 0:
        print(f'\nParabéns! Você adquiriu {diferenca_anos:0.2f} créditos de carbono.')
        print(f'Com isso, você receberá {valor_em_reais:0.2f} reais na venda desses créditos! ')
    elif diferenca_anos == 0:
        print('\nSeu consumo foi igual nos dois anos! Logo, você não adquiriu nenhum crédito de carbono.')
    else:
        diferenca_anos = abs(diferenca_anos)
        print(f'\nInfelizmente, suas emissões aumentaram em {diferenca_anos:.2f}!')
        print(f'Portanto, para compensar o aumento de emissões, '
              f'você deve comprar {diferenca_anos:0.2f} créditos de carbono!')
        print(f'Para isso, você deverá desembolsar {valor_em_reais:0.2f} reais.')


if __name__ == '__main__':
    main()
