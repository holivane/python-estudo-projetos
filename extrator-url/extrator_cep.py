
import re


endereco = "Rua das Flores 12, apartamento 101, Laranjeiras, Rio de Janeiro, RJ, 23440--120"

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)
else:
    raise ValueError("CEP não encontrado ou em formato incorreto.")
