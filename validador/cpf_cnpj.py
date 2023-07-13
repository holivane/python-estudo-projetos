from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Qunatidade de dígitos incorreta. Insira um CPF com 11 dígitos ou um CNPJ com 14 dígitos")

class DocCpf:
    def __init__(self, documento) -> None:
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF inválido!')

    def __str__(self) -> str:
        return self.format()

    def valida(self,documento):
        validador_cpf = CPF()
        return validador_cpf.validate(documento)

    def format(self):
        cpf_mask = CPF()
        return cpf_mask.mask(self.cpf)

class DocCnpj:
    def __init__(self, documento) -> None:
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ inválido!')

    def __str__(self) -> str:
        return self.format()

    def valida(self,documento):
        validador_cnpj = CNPJ()
        return validador_cnpj.validate(documento)

    def format(self):
        cnpj_mask = CNPJ()
        return cnpj_mask.mask(self.cnpj)


# class CpfCnpj:
#     def __init__(self, documento, tipo_documento) -> None:
#         self.tipo_documento = tipo_documento
#         documento = str(documento)
#         if self.tipo_documento == "cpf":
#             if self.cpf_valido(documento):
#                 self.cpf = documento
#             else:
#                 raise ValueError("CPF inválido!!!")
#         elif self.tipo_documento == "cnpj":
#             if self.cnpj_valido(documento):
#                 self.cnpj = documento
#             else:
#                 raise ValueError("CNPJ inválido!!!")
#         else:
#             raise ValueError("Documento inválido!")

#     def cpf_valido(self, cpf):
#         if len(cpf) == 11:
#             validador_cpf = CPF()
#             return validador_cpf.validate(cpf)
#         else:
#             raise ValueError("Quantidade de dígitos inválida!!")

#     def format_cpf(self):
#         cpf_mask = CPF()
#         return cpf_mask.mask(self.cpf)

#     def format_cnpj(self):
#         cnpj_mask = CNPJ()
#         return cnpj_mask.mask(self.cnpj)

#     def __str__(self) -> str:
#         if self.tipo_documento == 'cpf':
#             return self.format_cpf()
#         elif self.tipo_documento == 'cnpj':
#             return self.format_cnpj()

#     def cnpj_valido(self, cnpj):
#         if len(cnpj) == 14:
#             validador_cnpj = CNPJ()
#             return validador_cnpj.validate(cnpj)
#         else:
#             raise ValueError("Quantidade de dígitos inválida!!")