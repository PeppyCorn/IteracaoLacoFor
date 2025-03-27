lista_produtos = list()

def linha():
    print('=-' * 15)

def quantidade_de_produtos():
    linha()
    quantidade_produtos = int(input('Quantos produtos deseja cadastrar? '))
    linha()
    return quantidade_produtos

def desconto(valor_total):
    linha()
    deseja_desconto = input('Deseja aplicar desconto? [S/N] ').upper()
    if deseja_desconto == 'S':
        valor_desconto = int(input('Qual o valor do Desconto (em porcentagem)? '))
        novo_preco = valor_total - (valor_total * valor_desconto / 100)
        print(f'O valor total com desconto de {valor_desconto}% ficou R${novo_preco:.2f}')
    else:
        print('Sem desconto aplicado')

    linha()
    deseja_outra_operacao = input('Deseja Executar outra operação? [S/N] ').upper()
    if deseja_outra_operacao == 'S':
        lista_produtos.clear()
        produtos()


def produtos():
    for i in range(quantidade_de_produtos()):
        nome = input(f'Nome do Produto {i+1}? ')
        valor_produto = float(input(f'Qual o preço do(a) {nome}? '))
        lista_produtos.append( (nome, valor_produto) )

    print('\n--- Lista de Produtos ---')
    for nome, valor_produto in lista_produtos:
        print(f'{nome} - R$ {valor_produto:.2f}')

    total = 0
    for produto in lista_produtos:
        total += produto[1]

    print(f'\nTotal: R${total:.2f}\n')
    desconto(total)


produtos()

print('Fechando Caixa Registradora...')
linha()