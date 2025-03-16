import os

desktop = r'C:\Users\José Satiro\OneDrive\Desktop'
arquivo_caminho = os.path.join(desktop, 'tarefas.txt')

with open(arquivo_caminho, 'w') as arquivo:
    arquivo.write('1. Estudar python\n')
print('primeira tarefa adicionada')

with open(arquivo_caminho, 'r') as arquivo:
    conteudo = arquivo.read()
print('conteudo atual:')
print(conteudo)

with open(arquivo_caminho, 'a') as arquivo:
    arquivo.write('2. Fazer exercicius\n')
print('segunda tarefa adicionada')

with open(arquivo_caminho, 'r') as arquivo:
    conteudo_final = arquivo.read()
print('conteudo atualizado:')
print(conteudo_final)