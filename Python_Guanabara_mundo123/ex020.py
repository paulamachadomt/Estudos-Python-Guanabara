#sortear a ordem de apresentação dos nomes
import random
nome1 = input('digite o nome do primeiro aluno: ')
nome2 = input('digite o nome do segundo aluno: ')
nome3 = input('digite o nome do terceiro aluno: ')
nome4 = input('digite o nome do quarto aluno: ')
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print('a ordem de apresentação será:', lista)
