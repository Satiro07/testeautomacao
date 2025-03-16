import os
import shutil

desktop = r'C:\Users\José Satiro\OneDrive\Desktop'

print('caminho da area de trabalho: ',desktop)

arq_original = os.path.join(desktop, 'arquivo.txt')
print('Caminho do arquivo original: ',arq_original)

if not os.path.exists(arq_original):
    with open(arq_original, 'w') as arquivo:
        arquivo.write('Este é um arquivo teste!')
    print('Arquivo criado: ', arq_original)


if os.path.exists(arq_original):
    pasta_nova = os.path.join(desktop, 'MinhaPasta')
    os.makedirs(pasta_nova, exist_ok=True)
    print('Pasta criada: ', pasta_nova)

    arq_destino = os.path.join(pasta_nova, 'arquivo.txt')
    shutil.move(arq_original, arq_destino)
    print('Arquivo movido com sucesso! para: ',arq_destino)
else:
    print('Arquivo não encontrado')