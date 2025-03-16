import os

desktop = r'C:\Users\José Satiro\OneDrive\Desktop'

arq1 = os.path.join(desktop, 'notas.txt')

if not os.path.exists(arq1):
    with open(arq1, 'w') as arquivo:
        arquivo.write('Minhas notas importantes')
    
if os.path.exists(arq1):
    print('arquivo criado')
else:
    print('arquivo nao criado')