import pandas as pd
nomeanimais = {
    'bem-te-vi': {
        'nome': "Bem-te-vi",
        'tipo': "ave",
        'nomecientifico': "Pitangus sulphuratus"
    },
    'jiboia-arco-iris': {
        'nome': "Jiboia-arco-iris",
        'tipo': "reptil",
        'nomecientifico': "Epicrates cenchria"
    },
    'socozinho': {
        'nome': "Socozinho",
        'tipo': "ave",
        'nomecientifico': "Butorides striata"
    },
    'sanhaço-cinzento': {
        'nome': "sanhaço-cinzento",
        'tipo': "ave",
        'nomecientifico': "Thraupis sayaca"
    },
    'gavião-carijó': {
        'nome': "gavião-carijó",
        'tipo': "ave",
        'nomecientifico': "Rupornis magnirostris"
    },
    'urutau': {
        'nome': "urutau",
        'tipo': "ave",
        'nomecientifico': "Nyctibius griseus"
    },
    'coruja-buraqueira': {
        'nome': "coruja-buraqueira",
        'tipo': "ave",
        'nomecientifico': "Athene cunicularia"
    },
    'tamanduá-mirim': {
        'nome': "tamanduá-mirim",
        'tipo': "mamifero",
        'nomecientifico': "Tamandua tetradactyla"
    },
    'cassaco': {
        'nome': "cassaco",
        'tipo': "ave",
        'nomecientifico': "Cacicus haemorrhous"
    },
    'cagado-de-barbicha': {
        'nome': "cagado-de-barbicha",
        'tipo': "reptil",
        'nomecientifico': "Phrynops geoffroanus"
    },
    'corujinha-do-mato': {
        'nome': "corujinha-do-mato",
        'tipo': "ave",
        'nomecientifico': "Megascops choliba"
    },
    'carcará': {
        'nome': "carcará",
        'tipo': "ave",
        'nomecientifico': "Caracara plancus"
    },
    'galo-de-campina': {
        'nome': "galo-de-campina",
        'tipo': "ave",
        'nomecientifico': "Paroaria dominicana"
    },
    'chupim': {
        'nome': "chupim",
        'tipo': "ave",
        'nomecientifico': "Molothrus bonariensis"
    },
    'sanhaço-do-coqueiro': {
        'nome': "sanhaço-do-coqueiro",
        'tipo': "ave",
        'nomecientifico': "Tangara palmarum"
    },
    'batuqueiro': {
        'nome': "batuqueiro",
        'tipo': "ave",
        'nomecientifico': "Saltator similis"
    },
    'iguana-verde': {
        'nome': "iguana-verde",
        'tipo': "reptil",
        'nomecientifico': "Iguana iguana"
    },
    'coruja-suindara': {
        'nome': "coruja-suindara",
        'tipo': "ave",
        'nomecientifico': "Tyto furcata"
    },
    'jabuti-piranga': {
        'nome': "jabuti-piranga",
        'tipo': "reptil",
        'nomecientifico': "Chelonoidis carbonaria"
    },
    'golinho': {
        'nome': "golinho",
        'tipo': "ave",
        'nomecientifico': "Euphonia chlorotica"
    },
    'bacurau': {
        'nome': "bacurau",
        'tipo': "ave",
        'nomecientifico': "Nyctidromus albicollis"
    },
    'tatu peba': {
        'nome': "tatu peba",
        'tipo': "mamifero",
        'nomecientifico': "Euphractus sexcinctus"
    },
    'gato-maracajá': {
        'nome': "gato-maracajá",
        'tipo': "mamifero",
        'nomecientifico': "Leopardus wiedii"
    },
    'falcão quiriquiri': {
        'nome': "falcão quiriquiri",
        'tipo': "ave",
        'nomecientifico': "Falco sparverius"
    },
    'jiboia': {
        'nome': "jiboia",
        'tipo': "reptil",
        'nomecientifico': "Boa constrictor"
    },
    'periquito-de-encontro-amarelo': {
        'nome': "periquito-de-encontro-amarelo",
        'tipo': "ave",
        'nomecientifico': "Brotogeris chiriri"
    },
    'socó-dorminhoco': {
        'nome': "socó-dorminhoco",
        'tipo': "ave",
        'nomecientifico': "Nycticorax nycticorax"
    },
    'caburé': {
        'nome': "caburé",
        'tipo': "ave",
        'nomecientifico': "Glaucidium brasilianum"
    },
    'macaco-prego': {
        'nome': "macaco-prego",
        'tipo': "mamifero",
        'nomecientifico': "Sapajus libidinosus"
    },
    'sagui': {
        'nome': "sagui",
        'tipo': "mamifero",
        'nomecientifico': "Callithrix jacchus"
    },
    'galinha-d\'água': {
        'nome': "galinha-d'água",
        'tipo': "ave",
        'nomecientifico': "Gallinula chloropus"
    },
    'papagaio': {
        'nome': "papagaio",
        'tipo': "ave",
        'nomecientifico': "Amazona aestiva"
    },
    'veado-catingueiro': {
        'nome': "veado-catingueiro",
        'tipo': "mamifero",
        'nomecientifico': "Mazama gouazoubira"
    },
    'periquito-da-caatinga': {
        'nome': "periquito-da-caatinga",
        'tipo': "ave",
        'nomecientifico': "Eupsittula cactorum"
    }
}

op = int(input("Quantas operações você deseja adicionar? "))
nomenclaturaArray = []
nomeEspecieArray = []
nomecientificoArray = []
tipoArray = []
quantidadeArray = []
localArray = []
statusArray = []


def getStatus(status):
    if status == "1":
        return "Vivo"
    elif status == "2":
        return "Óbito"
    else:
        return getStatus(input("Status inválido. Digite novamente: "))
def getTipo(tipo):
    tipo = input(f"#{i}º operação: Qual o tipo? 1 para mamífero, 2 para ave, 3 para réptil ")
    if tipo == "1":
        return "mamífero"
    elif tipo == "2":
        return "ave"
    elif tipo == "3":
        return "réptil"
    else:
        return getTipo(input("Tipo inválido. Digite novamente: 1 para mamífero , 2 para ave, 3 para réptil "))



for i in range(1, op + 1):
    nomenclatura = input(f"#{i}º operação: Qual a Nomenclatura do caso ou operação? ")
    qEspecies = int(input(f"#{i}º operação: Quantas espécies você deseja adicionar? "))

    if qEspecies > 1:
        pass
    else:
        nomeEspecie = input(f"#{i}º operação: Qual o nome da espécie? ").lower()
        print(nomeEspecie)
        if nomeEspecie in nomeanimais:
            nome = nomeanimais[nomeEspecie]['nome']
            nomecientifico = nomeanimais[nomeEspecie]['nomecientifico']
            tipo = nomeanimais[nomeEspecie]['tipo']
            print('nome encontrado no banco de dados.')
        else:
            nome = nomeEspecie
            print("nome não encontrado no banco de dados.")
            nomecientifico = input(f"#{i}º operação: Qual o nome científico da espécie? ")
            tipo = getTipo(input(f"#{i}º operação: Qual o tipo? 1 para mamífero, 2 para ave, 3 para réptil "))
    status = getStatus(input(f"#{i}º operação: Qual o status? 1 para vivo, 2 para óbito "))
    if status == "Óbito":
        local = 0
    else :
        local = input(f"#{i}º operação: Qual o local da Soltura? ")
    quantidade = input(f"#{i}º operação: Quantos indivíduos da espécie? ")

    nomenclaturaArray.append(nomenclatura)
    nomeEspecieArray.append(nome)
    nomecientificoArray.append(nomecientifico)
    tipoArray.append(tipo)
    quantidadeArray.append(quantidade)
    localArray.append(local)
    statusArray.append(status)


dados = {
    'Nomenclatura do caso ou operação': nomenclaturaArray,
    'Nome Popular': nomeEspecieArray,
    'Nome Científico': nomecientificoArray,
    'Status': statusArray,
    'Quantidade de indivíduos da espécie': quantidadeArray,
    'Tipo': tipoArray,
    'Local da Soltura': localArray
}

df = pd.DataFrame(dados)

nome_arquivo = 'dados.xlsx'

try:
    df_existente = pd.read_excel(nome_arquivo)
    df_final = pd.concat([df_existente, df], ignore_index=True)
    df_final.to_excel(nome_arquivo, index=False)
    print(f"O arquivo '{nome_arquivo}' foi atualizado com sucesso.")
except FileNotFoundError:
    df.to_excel(nome_arquivo, index=False)
    print(f"O arquivo '{nome_arquivo}' foi criado com sucesso.")