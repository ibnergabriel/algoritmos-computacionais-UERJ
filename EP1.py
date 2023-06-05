def questao1():
    print("Questão 1: Contar quantidade de espaços e vogais em uma frase: ")
    qtd_branco = 0
    qtd_vogais = 0
    frase = input('Insira uma frase aqui: ')
    
    for letra in frase:
        if letra in 'aeiou':
            qtd_vogais +=1
        elif letra in ' ':
            qtd_branco +=1

    print(f'A quantidade de vogais na frase é: {qtd_vogais}')
    print(f'A quantidade de espaços em branco na frase é: {qtd_branco}')
    print()

def questao2():
    print("Questão 2: Pular linha a cada nova sequência")
    num_inteiro = int(input('Insira um número inteiro: '))
    i =  0
    lista = []
    while i < num_inteiro:
        i += 1
        lista.append(i)
        print(lista)

def questao3():
    print('Inverter número inserido: ')
    numero = int(input("Insira um número aqui: "))
    numeroInvertido = int(str(numero)[::-1])
    print(numeroInvertido)


def main():
    questao1()
    questao2()
    questao3()

main()