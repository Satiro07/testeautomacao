import os

nome_arquivo = input('Nome do arquivo com extensão (ex: notas.txt): ')
conteudo = input('O que deseja escrever: ')

desktop = r'C:\Users\José Satiro\OneDrive\Desktop'

caminho_arquivo = criar_arquivo = os.path.join(desktop, nome_arquivo)

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write(conteudo)
print(f'Arquivo {nome_arquivo} criado!')

with open(caminho_arquivo, 'r') as arquivo:
    mensagem = arquivo.read()
print('Conteudo do arquivo:')
print(mensagem)