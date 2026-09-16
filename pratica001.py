# Exercício 1 - Crie uma classe Cachorro com um __init__ que tenha dois atributos: nome e idade
# Depois crie dois objetos e dê valores diferentes para cada um.
class Cachorro:
    def __init__(self):
        self.nome = ""
        self.idade = 0

    # Exercício 2 - Na mesma classe cachorro, crie um método chamado latir() que retorne usando o nome do cachorro.
    def latir(self):
        return f"{self.nome} está latindo!"

    def mensagem(self):
        return f'{self.nome} tem {self.idade} anos'

c1 = Cachorro()
c1.nome = "Saori" 
c1.idade = 2
print(c1.mensagem())

c2 = Cachorro()
c2.nome = 'Rex'
c2.idade = 7
print(c2.latir())
print(c2.mensagem())

# Crie um objeto Cachorro, atribua uma idade a ele e depois altere essa idade.
# Depois imprima o objeto para confirmar a alteração.
c3 = Cachorro()
c3.nome = "Bettowen"
c3.idade = 5
c3.idade = 8
print(c3.mensagem())
print(f'{c3.nome} tem {c3.idade} anos')


# Exercício 4 -  Crie uma classe diferente de Gafanhoto e Cachorro
# ele deve ter pelo menos 2 atributos, pelo menos 1 método de instância, pelo menos 2 objetos dessa classe.

class Aluno:
    def __init__(self):
        self.nome = ""
        self.nota1 = 0
        self.nota2 = 0

    def mensagem(self):
        return f'{self.nome} tirou as notas {self.nota1} e {self.nota2}'

    def media(self):
        return f'E a sua média é de {(self.nota1 + self.nota2) / 2}' 



a1 = Aluno()
a1.nome = "Bruna"
a1.nota1 = 8
a1.nota2 = 9
print(a1.mensagem())
print(a1.media())  


a2 = Aluno()
a2.nome = "Guilherme"
a2.nota1 = 7
a2.nota2 = 6
print(a2.mensagem())
print(a2.media())

a3 = Aluno()
a3.nome = input('Qual o seu nome? ')
a3.nota1 = float(input('Qual a sua primeira nota: '))
a3.nota2 = float(input('Qual a sua segunda nota: '))
print(a3.mensagem())
print(a3.media())