from  datetime import datetime
class Funcionario:
    def __init__(self, nome, sobrenome, anoNascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.anoNascimento = anoNascimento
    def nomeCompleto(self):
        return self.nome + ' ' + self.sobrenome

    def idadeFuncionario(self):
        anoAtual = datetime.now().year
        self.anoNascimento = int(anoAtual - self.anoNascimento)
        return self.anoNascimento


usuario1 = Funcionario('elena', 'santos', 2000)
usuario2 = Funcionario('Mucillon', 'nogueira', 2007)

print(Funcionario.idadeFuncionario(usuario2))