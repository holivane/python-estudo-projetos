class Funcionario:
    def __init__(self, nome) -> None:
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostra_tarefas(self):
        print('Fez muita coisa...')

class Hipster:
    def __str__(self) -> str:
        return f'Hipster, {self.nome}'

class Caelum(Funcionario):
    def mostra_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Monstrando cursos - {mes}' if mes else 'Mostrando cursus desse mês')

class Alura(Funcionario):
    # def mostra_tarefas(self):
    #     print('Fez muita coisa, Alurete!')

    def busca_pergunta_sem_resposta(self):
        print(f'Mostrando perguntas não respondidas do fórum')

class Junior(Alura, Hipster):
    pass

class Pleno(Alura, Caelum, Hipster):
    pass

jose = Junior('José')
jose.busca_pergunta_sem_resposta()

luan = Pleno('Luan')
luan.busca_pergunta_sem_resposta()
luan.busca_cursos_do_mes()
luan.mostra_tarefas()

print(jose)
print(luan)