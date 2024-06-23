
# uvicorn main:app --reload

from fastapi import FastAPI
import pandas as pd
import requests
import io

app = FastAPI()

CSV_PRODUCAO = "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv"
CSV_PROCESSAMENTO = "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv"

@app.get("/")
def read_root():
    return {"message": "Welcome to the Embrapa viticulture API"}

@app.get("/producao")
def get_data_producao():
    try:
        # Fazer o download do CSV
        response = requests.get(CSV_PRODUCAO)
        response.raise_for_status()  # Levanta um erro se a requisição falhar

        data = pd.read_csv(io.StringIO(response.text), sep=';')

        # Preencher os valores NaN com None
        data = data.where(pd.notnull(data), None)

        data_dict = data.to_dict(orient='records')

        return {"data": data_dict}

        #return response.content
    except Exception as e:
        return {"error": str(e)}
        

@app.get("/processamento")
def get_data_processamento():
    try:
        # Fazer o download do CSV
        response = requests.get(CSV_PROCESSAMENTO)
        response.raise_for_status()  # Levanta um erro se a requisição falhar

        data = pd.read_csv(io.StringIO(response.text), sep=';')

        # Preencher os valores NaN com None
        data = data.where(pd.notnull(data), None)

        data_dict = data.to_dict(orient='records')

        return {"data": data_dict}

        #return response.content
    except Exception as e:
        return {"error": str(e)}