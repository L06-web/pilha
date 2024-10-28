def criar_pilha(tamanho):
    return [], tamanho

def empilhar(pilha, item, tamanho):
    if len(pilha) < tamanho:
        pilha.append(item)
        print(f"Item '{item}' empilhado com sucesso.")
    else:
        print("Erro: a pilha está cheia, não é possível empilhar.")

def desempilhar(pilha):
    if pilha:
        item = pilha.pop()
        print(f"Item '{item}' desempilhado com sucesso.")
    else:
        print("Erro: a pilha está vazia, não é possível desempilhar.")

def topo(pilha):
    if pilha:
        return pilha[-1]
    else:
        return "A pilha está vazia."

def main():
    tamanho = int(input("Defina o tamanho da pilha: "))
    pilha, max_tamanho = criar_pilha(tamanho)

    while True:
        print("\nEscolha uma operação: ")
        print("a) Empilhar")
        print("b) Desempilhar")
        print("c) Sair")

        opcao = input("Opção: ").lower()

        if opcao == 'a':
            item = input("Digite o item para empilhar: ")
            empilhar(pilha, item, max_tamanho)
        elif opcao == 'b':
            desempilhar(pilha)
        elif opcao == 'c':
            print("Topo da pilha:", topo(pilha))
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
