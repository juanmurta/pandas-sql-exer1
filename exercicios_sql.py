import sqlite3
import pandas as pd
import pyodbc

# conexão usando sqlite3
# conexao = sqlite3.connect('salarios.sqlite')
# tabela_salarios2 = pd.read_sql('SELECT * FROM Salaries', conexao)
# conexao.close()

# conexão usando pyodbc
dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=salarios.sqlite")
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

# Executa uma consulta SQL para selecionar todos os dados da tabela Salaries
cursor.execute('SELECT * FROM Salaries')
valores = cursor.fetchall()
descricao = cursor.description

# Fecha o cursor e a conexão com o banco de dados
cursor.close()
conexao.close()

# Cria uma lista com os nomes das colunas a partir da descrição
colunas = [tupla[0] for tupla in descricao]
# Cria um DataFrame do pandas com os valores recuperados e as colunas correspondentes
tabela_salarios = pd.DataFrame.from_records(valores, columns=colunas)

# filtrando somente san francisco
tabela_salarios = tabela_salarios.loc[tabela_salarios["Agency"] == "San Francisco", :]

tabela_sm = tabela_salarios[["Year", "TotalPay", "TotalPayBenefits"]].groupby("Year").mean()
print(tabela_sm)

# Agrupa os dados por ano e conta o número de registros
tabela_qtde = tabela_salarios.groupby("Year").count()
tabela_qtde = tabela_qtde[["Id"]]
tabela_qtde = tabela_qtde.rename(columns={"Id": "Quantidade"})
print(tabela_qtde)

def formatar(valor):
    return 'R${:.2f}'.format(valor)


# Agrupa os dados por ano e calcula a soma
tabela_total = tabela_salarios.groupby("Year").sum()
tabela_total = tabela_total[['TotalPay', 'TotalPayBenefits']]

# Aplica a formatação monetária às colunas de soma
tabela_total['TotalPay'] = tabela_total['TotalPay'].apply(formatar)
tabela_total['TotalPayBenefits'] = tabela_total['TotalPayBenefits'].apply(formatar)
print(tabela_total)
