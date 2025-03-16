import os
import shutil

desktop = r'C:\Users\José Satiro\OneDrive\Desktop'

conteudo = input('Digite algo: ')

arquivo_caminho = os.path.join(desktop, 'arquivo.txt')
print(arquivo_caminho)


with open(arquivo_caminho, 'w') as arquivo:
    arquivo.write(conteudo)

if os.path.exists(arquivo_caminho):
    pasta = os.path.join(desktop, 'PastaR')
    os.makedirs(pasta, exist_ok=True)

    arq_destino = os.path.join(pasta, 'arquivo.txt')
    shutil.move(arquivo_caminho, arq_destino)
    print('Deu certo')
else:
    print('Não deu certo')



