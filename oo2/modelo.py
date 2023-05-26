class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    def __str__(self):
        return f'Nome: {self.nome} - Likes: {self.likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas

    @property
    def listagem(self):
        return self.programas

    @property
    def tamanho(self):
        return len(self.programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()

listinha = [atlanta, demolidor, tmep, vingadores]
minha_playlist = Playlist('fim de semana', listinha)

for programa in minha_playlist.listagem:
    print(programa)

print(f'Tamanho: {minha_playlist.tamanho}')