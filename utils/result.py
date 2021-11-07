import numpy as np
import pandas as pd



def calculate_quartil(df):
    data = df.copy()
    
    q25 = data['prediction'].quantile(.25)
    q50 = data['prediction'].quantile(.5)
    q75 = data['prediction'].quantile(.75)
    
    return q25, q50, q75


def get_data_result(df):

    data = df.copy()

    # Vendas por loja
    df_result_1 = ( data[['store', 'prediction']]
                    .groupby('store')
                    .agg({'prediction': 'sum'})
                    .reset_index() )
    
    df_result_1['formatted_sales'] = df_result_1['prediction'].map('R$ {:,.2f}'.format)

    df_result_2 = ( ( df_result_1
                    .groupby('store')
                    .agg({'prediction': 'sum'}) / df_result_1['prediction'].sum() * 100 )
                    .reset_index()
                    .rename(columns={'prediction': 'percentage_sales'})
                  )

    df_result_full = pd.merge(df_result_1, df_result_2, how='inner', on='store')

    df_result_full['prediction'] = df_result_full['prediction'].map('{:.2f}'.format).astype(np.float64)

    def category_variable(x):
        q25, q50, q75 = calculate_quartil(df_result_full)
        
        if q25<=x<q50:
            return 'G3'
        elif q50<=x<q75:
            return 'G2'
        elif x >= q75:
            return 'G1'
        else:
            return 'G0'
    
    df_result_full['classification'] = df_result_full['prediction'].apply(lambda x: category_variable(x))

    return df_result_full