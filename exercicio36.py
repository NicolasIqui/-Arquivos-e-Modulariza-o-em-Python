
import os

dir = '/tmp/exercicios'
arq36 = 'ex36.txt'

def escreve_arq(caminho, arquivo, linha):
    if os.path.exists(caminho) and os.path.isdir(caminho):
        caminho_completo = caminho + '/' + arquivo
        if os.path.exists(caminho_completo):
            tipo = 'a'
        else:
            tipo = 'w'
        with open(caminho_completo, tipo, encoding='utf-8') as f:
            f.write(linha + '\n')

def fatorial(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    return fat

def divisao(a, b):
    return a / b

def main():
    os.makedirs(dir, exist_ok=True)
    os.chmod(dir, 0o744)

    n = int(input("digite um valor de um numero "))
    serie = 1

    for i in range(1, n + 1):
        fat = fatorial(i)
        termo = divisao(1, fat)
        serie += termo
        escreve_arq(dir, arq36, str(termo))

    escreve_arq(dir, arq36, "resultado:" + str(serie))

if __name__ == '__main__':
    main()
