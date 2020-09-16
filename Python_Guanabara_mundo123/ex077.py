#contagem de vogais de várias palavras dentro de uma tupla
listaPalavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for palavra in listaPalavras:
    print(f'\nNa palavra "{palavra}" temos as vogais ', end='')
    for letras in palavra:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')