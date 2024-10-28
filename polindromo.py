def empilhar(pilha, item):
    pilha.append(item)

def desempilhar(pilha):
    return pilha.pop() if pilha else None

def eh_palindromo(texto):
    pilha = []
    texto = texto.replace(" ", "").lower() 

    for char in texto:
        empilhar(pilha, char)
    inverso = ''.join([desempilhar(pilha) for _ in range(len(texto))])

    return texto == inverso

def main():
    texto = input("Digite a palavra ou frase para verificar se é um palíndromo: ")
    if eh_palindromo(texto):
        print(f"'{texto}' é um palíndromo.")
    else:
        print(f"'{texto}' não é um palíndromo.")

if __name__ == "__main__":
    main()
