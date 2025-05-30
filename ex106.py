from time import sleep
c = ('\033[m',         #0 - sem cor
     '\033[0;30;41m',  #1 - vermelho
     '\033[0;30;42m',  #2 - verde
     '\033[0;30;43m',  #3 - amarelo
     '\033[0;30;44m',  #4 - azul
     '\033[0;30;45m',  #5 - roxo
     '\033[7;30m'      #6 - branco
     );

def ajuda (com):
    titulo(f'acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor = 0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print(c[0], end='')
    sleep(1)


comando =''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input("funcao ou biblioteca> "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ate logo', 1)