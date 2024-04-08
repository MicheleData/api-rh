from flask import Flask
import pandas as pd

df_rh = pd.read_excel("BaseFuncionarios.xlsx")


app = Flask(__name__)

@app.route("/")
def rh():
    
    df_rh_json = df_rh.to_json()

    return df_rh_json

    

if __name__ == '__main__':
    app.run()