import requests


# Função para pesquisar o nome científico de um animal
def pesquisar_nome_cientifico(animal):
    url = f"https://api.aniimal.com/scientific-name?animal={animal}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        nome_cientifico = data['scientific_name']
        print(f"O nome científico de '{animal}' é: {nome_cientifico}")
    else:
        print(f"Não foi possível obter o nome científico de '{animal}'.")

pesquisar_nome_cientifico("cavalo")
