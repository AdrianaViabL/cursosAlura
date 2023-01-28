class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter  # definindo como os valores serao atribuidos a variavel nome (especialização)
    def nome(self, new_nome):
        self._nome = new_nome.title()

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} likes'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):  # sobrepondo o init da classe mae, mas...
        super().__init__(nome, ano)  # ainda usando parte do que é trazido da herança
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - duração: {self.duracao} - {self._likes} likes'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):  # representação textual da parte do codigo
        return f'{self._nome} - {self.ano} - temporadas: {self.temporadas} - {self._likes} likes'


class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
demolidor = Serie('Demolidor', 2018, 3)
atlantis = Filme('atlantis', 2005, 95)
atlanta.dar_like()
atlantis.dar_like()
atlantis.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()

print('==='*50)
movies_and_serie = [atlanta, vingadores, demolidor, atlantis]

weekend_list = Playlist('fim de semana', movies_and_serie)
print(type(movies_and_serie))
for program in weekend_list:
    print(program)

print('==='*50)
