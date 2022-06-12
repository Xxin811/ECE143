import pandas as pd
def add_month_yr(x):
    '''
    This function can take in the x survey dataframe and then output the same dataframe with a new month-yr column
    :param x: x is a pd.Series
    :return: pd.DataFrame object
    '''
    assert isinstance(x,pd.DataFrame)
# df = pd.read_csv('survey_data.csv',squeeze = True)
# df = df.loc[:, ['ID','Timestamp']]
# df = df.set_index('ID')
    x['month-yr'] = pd.to_datetime(x['Timestamp']).dt.strftime('%b-%Y')
# df = df.loc[:, ['month-yr']]
    return x
# print(df)

