import os

dir = '/tmp/exercicios'
arq38 = 'ex38.txt'
arq_mult5 = 'multiplos5.txt'

def escreve_arq(caminho, arquivo, linha):
    if os.path.exists(caminho) and os.path.isdir(caminho):
        caminho_completo = caminho + '/' + arquivo
        if os.path.exists(caminho_completo):
            tipo = 'a'
        else:
            tipo = 'w'
        with open(caminho_completo, tipo, encoding='utf-8') as f:
            f.write(linha + '\n')

def ex1():
    contador = 1
    maior = None
    menor = None

    while contador <= 10:
        n = int(input("Digite um número: "))
        escreve_arq(dir, arq38, str(n))

        if contador == 1:
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n

        contador += 1

    escreve_arq(dir, arq38, "maior:" + str(maior))
    escreve_arq(dir, arq38, "menor:" + str(menor))

def ex2():
    caminho = dir + '/' + arq38

    if os.path.exists(caminho):
        with open(caminho, 'r', encoding='utf-8') as f:
            for linha in f:
                linha = linha.strip()
                if "maior" not in linha and "menor" not in linha:
                    num = int(linha)
                    if num % 5 == 0:
                        escreve_arq(dir, arq_mult5, str(num))

def main():
    os.makedirs(dir, exist_ok=True)
    os.chmod(dir, 0o744)
    ex1()
    ex2()

if __name__ == '__main__':
    main()  


