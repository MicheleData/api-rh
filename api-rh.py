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

    df_rh = pd.DataFrame(dados)
    dic_df_rh = df_rh.to_json()
    return dic_df_rh

if __name__ == '__main__':
    app.run()