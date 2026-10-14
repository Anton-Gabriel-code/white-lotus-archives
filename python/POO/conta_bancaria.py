class SuperHeroi:
    def __int__(self, nome, idade, poder):
        self.nome = nome
        self.idade = idade
        self.poder = poder
    def mensagem(self):
        return f'Bem-Vindo Super Heroi:\nNome: {self.nome}\nIdade: {self.idade}\nHabilidade (Poder): {self.poder}'

