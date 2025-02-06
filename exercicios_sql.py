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

cursor.execute('SELECT * FROM Salaries')
valores = cursor.fetchall()
descricao = cursor.description

# print(valores[:10])
# print(descricao)
cursor.close()
conexao.close()

colunas = [tupla[0] for tupla in descricao]
tabela_salarios = pd.DataFrame.from_records(valores, columns=colunas)

# print(valores[:10])
# print(descricao)

# filtrando somente san francisco
tabela_salarios = tabela_salarios.loc[tabela_salarios["Agency"] == "San Francisco", :]

tabela_sm = tabela_salarios[["Year", "TotalPay", "TotalPayBenefits"]].groupby("Year").mean()
print(tabela_sm)


tabela_qtde = tabela_salarios.groupby("Year").count()
tabela_qtde = tabela_qtde[["Id"]]
tabela_qtde = tabela_qtde.rename(columns={"Id": "Quantidade"})
print(tabela_qtde)

def formatar(valor):
    return 'R${:.2f}'.format(valor)

tabela_total = tabela_salarios.groupby("Year").sum()
tabela_total = tabela_total[['TotalPay', 'TotalPayBenefits']]
tabela_total['TotalPay'] = tabela_total['TotalPay'].apply(formatar)
tabela_total['TotalPayBenefits'] = tabela_total['TotalPayBenefits'].apply(formatar)
print(tabela_total)
