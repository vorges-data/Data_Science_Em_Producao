import os

import pandas as pd
from fastapi import FastAPI

from db import database
from logger import log_config
from preprocessing import Rossmann

# Abre conexão com o banco de dados
conn = database()

# Extração das bases de dados de vendas da Rossmann
db = conn['rossmann']
predictions = db.predictions

# Configurações de log
logger = log_config()

# Instância do FastAPI
app = FastAPI(title='API Prediction sales Rossmann', description='API for prediction sales the stores at Rossmann', versão='1.0')


@app.get('/predictions')
async def get_predictions():
    try:
        items = [store for store in predictions.find({}, {"_id": False})]
        return items
    except Exception as e:
        logger.error(e)


@app.get('/prediction/{store}')
async def get_prediction(store: int):
    
    try:
        store_found = predictions.find_one({"store": store}, {"_id": False})

        if store_found:
            logger.info(f"Status code 200 - Loja {store} encontrada")
            return store_found
        else:
            logger.info(f'Status code 400 - Loja {store} não encontrada')
            return {'Message': f'Loja {store} não encontrada'}
    except Exception as e:
        logger.error(e)

