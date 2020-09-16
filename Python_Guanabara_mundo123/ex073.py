#Fatiamento de tuplas
times = ('corinthians', 'palmeiras', 'santos', 'grêmio', 'cruzeiro', 'flamengo', 'vasco',
        'chapecoense', 'atlético', 'botafogo', 'atlético-pr', 'bahia', 'são paulo',
        'fluminese', 'sport recife', 'ec vitória', 'coritiba', 'avaí', 'ponte preta',
        'atlético-go')
print('-'*120) 
print(f'Lista de times: {times}') 
print('-'*120)   
print(f'Os 5 primeiros colocados: {times[0:5]}') 
print('-'*120) 
print(f'Os 4 últimos colocados: {times[-4:]}')    
print('-'*120)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-'*120)
print(f'O chapecoense está na {times.index("chapecoense")+1}ª posição.')
print('-'*120)