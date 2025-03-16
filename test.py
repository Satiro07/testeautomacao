import os


desktop = os.path.join(os.path.expanduser('~'), 'Desktop')

print('caminho da area de trabalho: ',desktop)

arq_original = os.path.join(desktop, 'arquivo.txt')
print('Caminho do arquivo original: ',arq_original)

if not os.path.exists(arq_original):
    with open(arq_original, 'w') as arquivo:
        arquivo.write('Este é um arquivo teste!')
    print('Arquivo criado: ', arq_original)

if os.path.exists(arq_original):
    print('Arquivo movido com sucesso!')
else:
    print('Arquivo não encontrado')