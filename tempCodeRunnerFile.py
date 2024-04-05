from flask import Flask
import pandas as pd
import pyodbc

dados_conexao = ("Driver={SQL Server};"
                    "Server=DESKTOP-DFB74LT;"
                    "DataBase=Base_RH")
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()


app = Flask(__name__)

@app.route("/")
def rh():
    comando = f""" SELECT * FROM Tabela_base
"""
    
    cursor.execute(comando)
    dados = cursor.fetchall()
    descricao = cursor.description
    colunas = [tupla[0] for tupla in descricao]

    df_rh = pd.DataFrame.from_records(dados, columns=colunas)
    df_rh_json = df_rh.to_json()

    return df_rh_json

    

if __name__ == '__main__':
    app.run()