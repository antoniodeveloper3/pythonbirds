class Pessoa:  # Classe
    olhos = 2

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
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(renzo.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos),id(luciano.olhos),id(renzo.olhos),)


