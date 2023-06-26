import pandas as pd

# Criando um dicionário com os dados
op = int(input("quantas operações vc quer adicionar ?"))
nomenclatutraArray = []
nomeEspecieArray = []
tipoArray = []
quantidadeArray = []
localArray = []
statusArray = []
for i in range(1, op+1):
    nomenclatura = input(f"#{i}º operação: qual a Nomenclatura do caso ou operação")
    qEspecies = int(input(f"#{i}º operação: quantas especies vc quer adicionar ?"))
    if qEspecies > 1:
        pass
    else:
        nomeEspecie = input(f"#{i}º operação: qual o nome da espécie")
    tipo = input(f"#{i}º operação: qual o tipo? 1 para mamifero, 2 para ave, 3 para reptil")
    if tipo == "1":
        tipo = "mamifero"
    elif tipo == "2":
        tipo = "ave"
    elif tipo == "3":
        tipo = "reptil"
    quantidade = input(f"#{i}º operação: quantos individuos da espécie")
    status= input(f"#{i}º operação: qual o status? 1 para vivo, 2 para Óbito")
    if status == "1":
        status = "Vivo"
        local = input(f"#{i}º operação: qual o local")

    elif status == "2":
        status = "Óbito"
        local = 0
    else:
        print("status invalido")

    nomenclatutraArray.append(nomenclatura)
    nomeEspecieArray.append(nomeEspecie)
    tipoArray.append(tipo)
    quantidadeArray.append(quantidade)
    localArray.append(local)
    statusArray.append(status)
dados = {
    'Nomenclatura do caso ou operação': nomenclatutraArray,
    'nome da espécie': nomeEspecieArray,
    'quantos individuos da espécie': quantidadeArray,
    'tipo': tipoArray,
    'status': statusArray,
    'local': localArray
}

# Criando o DataFrame a partir do dicionário
df = pd.DataFrame(dados)

# Salvando o DataFrame em um arquivo Excel
nome_arquivo = 'dados.xlsx'
df.to_excel(nome_arquivo, index=False)

print(f"O arquivo '{nome_arquivo}' foi criado com sucesso.")
