from classes import Grafo, Vertice
from time import sleep

def title(text):
    print('-' * 40)
    print(text)
    print('-' * 40)

def display_menu():
    print('=' * 70)
    print('Menu')
    print('=' * 70)
    print('[1] Adicionar vértice')
    print('[2] Adicionar aresta entre vertices.')
    print('[3] Exibir vertices')
    print('[4] Sair')
    print('=' * 70)
    option = input('Escolha alguma opção: ')
    return option

def init_option():
    # sleep(0.5)
    print('=' * 40)

def adicionar_vertice(grafo):
    init_option()

    # getting vertex key
    while True:
        key = input('Digite uma chave para o vértice: ')
        
        if grafo.key_exists(key):
            title(f'A chave ({key}) já existe dentro do grafo.')
            # sleep(1.3)
            continue
        else:
            grafo.add_vertice(key)
            title(f'Vertice ({key}) adicionado')
            break
        
    # displaying vertex's
    exibir_vertices(grafo)

def adicionar_aresta(grafo):
    init_option()

    # getting first vertex
    while True:
        key1 = input('Primeiro vertice: ')

        if grafo.key_exists(key1):
            break

        print(f'Key ({key1}) inexistente. Tente novamente.')
        # sleep(0.5)
    
    # getting second vertex
    while True:
        key2 = input('Segundo vertice: ')

        if grafo.key_exists(key2):
            break

        print(f'Key ({key2}) inexistente. Tente novamente.')
        # sleep(0.5)
    
    # getting weight (optional)
    while True:
        weight = input('Informe o peso da ligação (Pressione "Enter" utilizar o valor padrão):')

        if weight == '':
            weight = 1
            break

        try:
            weight = int(weight)
            break
        except:
            print(f'Valor inválido. Tente um número inteiro.')
    
    # binding vertex's
    grafo.liga_vertices(key1, key2, weight)
    
    # displaying vertex's
    exibir_vertices(grafo)


def exibir_vertices(grafo):
    title('Exibindo vertices')

    for s in grafo.str_all_vertices():
        # sleep(0.3)
        print(s)
    
    # sleep(1.5)
    

def main():
    grafo = Grafo()

    while True:
        option = display_menu()

        if option == '1':
            adicionar_vertice(grafo)
        elif option == '2':
            adicionar_aresta(grafo)
        elif option == '3':
            exibir_vertices(grafo)
        elif option == '4':
            title('Saindo...')
            # sleep(0.5)
            break
        else:
            print(f'Opção inválida. Tente novamente.')    

if __name__ == "__main__":
    main()