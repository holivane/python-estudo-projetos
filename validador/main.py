from cpf_cnpj import Documento
from validate_docbr import CNPJ

exemplo_cnpj = "35379838000112"
exemplo_cpf = "56131763020"
# cnpj = CNPJ()
# print (cnpj.validate(exemplo_cnpj))

documento = Documento.cria_documento(exemplo_cnpj)
documento2 = Documento.cria_documento(exemplo_cpf)

print(documento)
print(documento2)