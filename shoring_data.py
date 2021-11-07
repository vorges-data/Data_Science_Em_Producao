import os

import pandas as pd


from db import database
from utils import get_data_result
from preprocessing import Rossmann

# Manipulação de diretórios
BASE_DIR = os.path.join(os.path.abspath('.'))
MODELS_DIR = os.path.join(BASE_DIR, 'models')
model = pd.read_pickle(os.path.join(MODELS_DIR, 'models.pkl'))


# Abre conexão com o banco de dados
conn = database()

# Extração das bases de dados de vendas da Rossmann
db = conn['rossmann']
sales = db.test
store = db.store
predictions = db.predictions


# Prepara dos dados para predição
rossmann = Rossmann()


def dataset():
    df_sales = pd.DataFrame.from_dict(data=sales.find({}, projection={'_id': False}))
    df_store = pd.DataFrame.from_dict(data=store.find({}, projection={'_id': False}))

    data = pd.merge(df_sales, df_store, how='left', on='Store')

    return data


def shoring():
    
    data = dataset()
    data = rossmann.pipeline(data)[model['features_selected']]

    pred = model['model'].predict(data)

    data['prediction'] = pred ** 3

    data = get_data_result(data)
    
    predictions.insert_many(data.to_dict('records'))

    return 1

if __name__ == '__main__':
    shoring()