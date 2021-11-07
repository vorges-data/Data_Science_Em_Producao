import time
from datetime import datetime, timedelta

import inflection
import numpy as np
import pandas as pd

from .transformers import sin, cos

class Rossmann:


    def __init__(self):
        pass


    def pipeline(self, df):
        
        data = df.copy()

        # Realiza do pré-processamento e limpeza dos dados
        data = self.__preparing_data(data)

        # Realiza a construção de novas variáveis
        data = self.__feature_engineering(data)

        # Realiza transformações nas variáveis sazonais
        data = self.__nature_transformation(data)

        return data


    def __cols_snakecase(self, df):
        old_cols = df.columns.tolist()
        snakecase = lambda x: inflection.underscore(x)
        new_cols = list(map(snakecase, old_cols))

        #rename columns
        df.columns = new_cols
        
        return df


    def __preparing_data(self, df):
    
        data = df.copy()

        data = self.__cols_snakecase(data)
        
        data = data.loc[data['open'] != 0]
        
        # transformer column date to datetime
        data['date'] = pd.to_datetime(data['date'])
        
        # competition_distance
        data['competition_distance'] = data['competition_distance'].apply(lambda x: 200000.0 if np.isnan(x) else x)

        # competition_open_since_month
        data['competition_open_since_month'] = data.apply(
            lambda x: x['date'].month if np.isnan(x['competition_open_since_month']) else x['competition_open_since_month']
        , axis=1)

        # competition_open_since_year
        data['competition_open_since_year'] = data.apply(
            lambda x: x['date'].year if np.isnan(x['competition_open_since_year']) else x['competition_open_since_year']
        , axis=1)

        # promo2_since_week
        data['promo2_since_week'] = data.apply(
            lambda x: x['date'].week if np.isnan(x['promo2_since_week']) else x['promo2_since_week']
        , axis=1)

        # promo2_since_year
        data['promo2_since_year'] = data.apply(
            lambda x: x['date'].year if np.isnan(x['promo2_since_year']) else x['promo2_since_year']
        , axis=1)

        # promo_interval
        data['promo_interval'].fillna(0, inplace=True)
        
        # correcting data types
        data['competition_open_since_month'] = data['competition_open_since_month'].astype(np.int32)
        data['competition_open_since_year'] = data['competition_open_since_year'].astype(np.int32)

        data['promo2_since_week'] = data['promo2_since_week'].astype(np.int32)
        data['promo2_since_year'] = data['promo2_since_year'].astype(np.int32)
        
        return data


    

    def __feature_engineering(self, df):
    
        data = df.copy()
        
        months = {
            1: 'jan',
            2: 'fev',
            3: 'mar',
            4: 'apr',
            5: 'may',
            6: 'jun',
            7: 'jul',
            8: 'aug',
            9: 'sep',
            10: 'oct',
            11: 'nov',
            12: 'dec'
        }
        

        # year
        data['year'] = data['date'].dt.year

        # month
        data['month'] = data['date'].dt.month

        # day
        data['day'] = data['date'].dt.day

        # week of year
        data['week_of_year'] = data['date'].dt.isocalendar().week.astype(np.int32)

        # year week
        data['year_week'] = data['date'].dt.strftime('%Y-%W')

        # competition since
        data['competition_since'] = data.apply(
            lambda x: datetime(year=x['competition_open_since_year'], month=x['competition_open_since_month'], day=1)
        , axis=1)

        data['competition_time_month'] = ((data['date'] - data['competition_since'])/30).apply(lambda x: x.days).astype(np.int)

        # promo since
        data['promo_since'] = data['promo2_since_year'].astype(str) + '-' + data['promo2_since_week'].astype(str)
        data['promo_since'] = data['promo_since'].apply(lambda x: datetime.strptime(x + '-1', '%Y-%W-%w') - timedelta(days=7))
        data['promo_time_week'] = ((data['date'] - data['promo_since'])/7).apply(lambda x: x.days).astype(np.int)

        # assortment
        data['assortment'] = data['assortment'].map({'a': 'basic', 'b': 'extra', 'c': 'extended'})

        # state holiday
        data['state_holiday'] = data['state_holiday'].map({'a': 'public holiday', 'b': 'Easter holiday', 'c': 'Christimas', 0: 'regular day'})
        

        #is_promo
        data['cat_month'] = data['date'].dt.month.map(months)
        
        data['is_promo'] = data[['promo_interval', 'cat_month']].apply(
            lambda x: 0 if x['promo_interval'] == 0 else 1 if x['cat_month'] in x['promo_interval'].lower().split(',') else 0
        , axis=1)
        
        data = data.drop(['promo_interval', 'cat_month'], axis=1)
        
        return data


    def __nature_transformation(self, df):
    
        data = df.copy()
        
        # day of week
        data['day_of_week_sin'] = data['day_of_week'].apply(lambda x: sin(x, 7))
        data['day_of_week_cos'] = data['day_of_week'].apply(lambda x: cos(x, 7))

        #month
        data['month_sin'] = data['month'].apply(lambda x: sin(x, 12))
        data['month_cos'] = data['month'].apply(lambda x: cos(x, 12))

        # day
        data['day_sin'] = data['day'].apply(lambda x: sin(x, 30))
        data['day_cos'] = data['day'].apply(lambda x: cos(x, 30))

        # week of year
        data['week_of_year_sin'] = data['week_of_year'].apply(lambda x: sin(x, 52))
        data['week_of_year_cos'] = data['week_of_year'].apply(lambda x: cos(x, 52))
        
        return data




