import os
import shutil

desktop = r'C:\Users\José Satiro\OneDrive\Desktop'

nome = input('escreva o nome do arquivo com a extensão (.py): ')
conteudo = input('Digite algo: ')

arquivo_caminho = os.path.join(desktop, nome)
print(arquivo_caminho)


with open(arquivo_caminho, 'w') as arquivo:
    arquivo.write(conteudo)

if os.path.exists(arquivo_caminho):
    pasta = os.path.join(desktop, 'PastaR')
    os.makedirs(pasta, exist_ok=True)

    arq_destino = os.path.join(pasta, 'Subpasta')
    
    arq = os.path.join(arq_destino, nome)
    shutil.move(arquivo_caminho, arq)
    
    print('Deu certo')
else:
    print('Não deu certo')

with open(arq, 'r') as arquivo:
    mensagem = arquivo.read()
print('Conteudo: ')
print(mensagem)