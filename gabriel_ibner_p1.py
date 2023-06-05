def questao1():
    print("Questão 1")
    print()
    qtd_consoantes = 0
    qtd_vogais = 0
    qtd_branco = 0
    qtd_caracteres = 0
    frase = input('Insira uma frase aqui: ')
    
    for letra in frase:
        if letra in 'aeiou':
            qtd_vogais +=1
        elif letra in ' ':
            qtd_branco +=1
        else:
            qtd_consoantes +=1

    print(f'A quantidade de vogais na frase é: {qtd_vogais}')
    print(f'A quantidade de consoantes na frase é: {qtd_consoantes}')
    print()

    qtd_caracteres = qtd_vogais + qtd_consoantes + qtd_branco
    print(f'A quantidade de caracteres na frase é: {qtd_caracteres}')
    # A quantidade de caracteres conta com os espaços em branco


def questao2():
    print("Questão 2")
    print()
    num_inteiro = int(input('Insira um número inteiro: '))
    j =  0
    primo = 0
    lista = []

    for i in range(1, num_inteiro + 1):        
        if num_inteiro % i == 0:
            primo += 1


    if primo != 2:
        while j < num_inteiro:
            j += 1
            lista.append(j)
    else:
        print("Número lido é primo, função não pode ser executada!")

    print(lista[::-1])
    print()

def questao3():
    print('Questão 3')
    print()
    numero = int(input("Insira um número aqui: "))
    numeroInvertido = int(str(numero)[::-1])
    print(numeroInvertido)

def main():
    questao1()
    questao2()
    questao3()

main()