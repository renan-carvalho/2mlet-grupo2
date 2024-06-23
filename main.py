
# uvicorn main:app --reload

from fastapi import FastAPI
import pandas as pd
import requests
import io

app = FastAPI()

CSV_PRODUCAO = "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv"
CSV_PROCESSAMENTO = "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv"
CSV_COMERCIALIZACAO = "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv"
CSV_IMPORTACAO = "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv"
CSV_EXPORTACAO = "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv"

@app.get("/")
def read_root():
    return {"message": "Welcome to the Embrapa viticulture API"}

def fetch_and_process_csv(url: str):
    response = requests.get(url)
    response.raise_for_status()  # Levanta um erro se a requisição falhar
    data = pd.read_csv(io.StringIO(response.text), sep=';', encoding='utf-8')
    data = data.replace([pd.NA, pd.NaT, float('inf'), float('-inf')], None) # Preencher valores NaN e infinitos com None
    return data.to_dict(orient='records')

@app.get("/producao")
def get_data_producao():
    try:
        data_dict = fetch_and_process_csv(CSV_PRODUCAO)
        return {"data": data_dict}
    except Exception as e:
        return {"error": str(e)}

@app.get("/processamento")
def get_data_processamento():
    try:
        data_dict = fetch_and_process_csv(CSV_PROCESSAMENTO)
        return {"data": data_dict}
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/comercializacao")
def get_data_comercializacao():
    try:
        data_dict = fetch_and_process_csv(CSV_COMERCIALIZACAO)
        return {"data": data_dict}
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/importacao")
def get_data_importacao():
    try:
        data_dict = fetch_and_process_csv(CSV_IMPORTACAO)
        return {"data": data_dict}
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/exportacao")
def get_data_exportacao():
    try:
        data_dict = fetch_and_process_csv(CSV_EXPORTACAO)
        return {"data": data_dict}
    except Exception as e:
        return {"error": str(e)}