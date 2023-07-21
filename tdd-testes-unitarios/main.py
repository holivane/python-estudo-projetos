from codigo.bytebank import Funcionario


def teste_idade():
    funcionario_teste = Funcionario('Teste', '13/03/2000', 1200)
    print(f'Teste = {funcionario_teste.idade()}')

    funcionario_teste1 = Funcionario('Teste', '13/03/1999', 1000)
    print(f'Teste = {funcionario_teste1.idade()}')

    funcionario_teste2 = Funcionario('Teste', '01/12/1988', 2000)
    print(f'Teste = {funcionario_teste2.idade()}')


teste_idade()
