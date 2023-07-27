from codigo.bytebank import Funcionario

ana = Funcionario('Ana', '12/07/2000', 1000)
maria = Funcionario('Maria', '12/07/2000', 10000)
jorge = Funcionario('Jorge', '12/07/2000', 100000)

nomes = [ana, maria, jorge]

for nome in nomes:
    try:
        print(('O bônus da {} é {}').format(nome.nome, nome.calcular_bonus()))
    except Exception as e:
        print(f'Erro ao clacular o bônus para {nome.nome}: {e}')
