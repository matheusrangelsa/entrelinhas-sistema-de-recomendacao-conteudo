import pandas as pd
import os
from time import sleep


# Leitura do dataset de filmes
dataset = pd.read_csv('filmes_projeto.csv') # removendo a pasta anterior e alocando na pasta atual



os.system('cls' if os.name == 'nt' else 'clear') # Codigo para limpar a tela ao iniciar o programa

# recebendo input do user
duracao_tempo_trajeto = int(input('\n\nInforme o tempo do seu trajeto no metrô em minutos (apenas números): '))

# seleção de categorias
def genero():
    # Imprime as opções de gênero
    print('\n ---------- SELECAO DE GENEROS ------------\n')

    options = {
        'Genero': 'Acao,Comedia,Drama,Ficcao Cientifica,Romance,Suspense,Terror'.split(','),
        'Codigo': [int(i) for i in range(1, 8)] # isso aqui pode ser automatizado usando um len() pra ver quantos generos existem
    }

    choices = []

    genres = pd.DataFrame(data = options)
    # formatando a saída para escolha dos generos
    print(genres.to_string(index = False))
    
    # Lê a seleção de gêneros feita pelo usuário
    selected = input('\nEscolha os gêneros abaixo digitando os número correspondentes separados por vírgula: ').replace(' ', '').split(",") # tratando a entrada do usuario
    selected_options = []

    # Verifica se a seleção do usuário é válida e adiciona à lista de gêneros escolhidos
    for s in selected:
      if int(s) in list(genres.Codigo):
        g = genres[genres.Codigo == int(s)].Genero.unique()[0]
        selected_options.append(g)

    # Imprime a lista de gêneros escolhidos ou uma mensagem de erro caso não haja seleções válidas
    if selected_options:
        genres_selected = genres.loc[genres.Genero.isin(selected_options)]
        print("\n --------- Opções selecionadas ----------- \n")
        print(genres_selected.to_string(index = False))
        print("\n ----------------------------------------- \n")
        sleep(2)
    else:
        print("Nenhuma opção válida selecionada.")
    
    return selected_options

# Chamando a função para executá-la  ****ESSE TIPO DE COMENTARIO ACABA SENDO UM POUCO INUTIL E POLUI O CODIGO****
lista_generos = genero()


# Primeiro filtro do dataset com base nos critérios de duração e categorias
def filter_movies(dataset, lista_generos, duracao_tempo_trajeto):
    # Cria uma lista vazia para armazenar os filmes filtrados
    f = (dataset.Categoria.isin(lista_generos)) & (dataset.Duracao <= duracao_tempo_trajeto)
    dataset = dataset.loc[f]
    return dataset

# Armazenamento dos resultados da função
dataset_movies_filtered = filter_movies(dataset, lista_generos, duracao_tempo_trajeto)


for i in range(0, 4):
    os.system('cls' if os.name == 'nt' else 'clear')    
    print('Gerando a sua lista de recomendacoes...')
    print('')
    print((i*(i*5)) * '#')
    sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')
print('\n------------ SUA LISTA DE RECOMENDACOES --------------------\n')
print(dataset_movies_filtered.to_string(index = False))
print('\n\n')