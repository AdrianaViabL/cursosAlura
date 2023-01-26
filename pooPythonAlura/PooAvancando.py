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

    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self._likes} likes')


class Filme(Programa):
    def __init__(self, nome, ano, duracao):  # sobrepondo o init da classe mae, mas...
        super().__init__(nome, ano)  # ainda usando parte do que é trazido da herança
        self.duracao = duracao

    def imprime(self):
        print(f'{self._nome} - {self.ano} - duração: {self.duracao} - {self._likes} likes')


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprime(self):
        print(f'{self._nome} - {self.ano} - temporadas: {self.temporadas} - {self._likes} likes')


vingadores = Filme('vingadores - guerra infinita', 2018, 160)

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()

print('==='*50)
movies_and_serie = [atlanta, vingadores]
for program in movies_and_serie:
    program.imprime()

print('==='*50)