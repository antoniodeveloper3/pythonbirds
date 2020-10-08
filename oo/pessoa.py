class Pessoa:  # Classe
    def __init__(self, *filhos, nome=None, idade=35):  # Atributos da Classe
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)  # atributo complexo

    def cumprimentar(self):  # Metódo da Classe
        return f'Olá {id(self)}'  # O método executa alguma coisa.

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    print(luciano.__dict__)
    print(renzo.__dict__)
