import pandas as pd
def add_month_yr(x):
    '''
    This function can take in the x survey dataframe and then output the same dataframe with a new month-yr column
    :param x: x is a pd.Series
    :return: pd.DataFrame object
    '''
    assert isinstance(x, pd.DataFrame)
    x['month-yr'] = pd.to_datetime(x['Timestamp']).dt.strftime('%b-%Y')
    return x

def fix_categorical(x):
    '''

    :param x: x is a DataFrame
    :return: pd.DataFrame with the "month-yr" column having the categorical dtype
    '''
    assert isinstance(x, pd.DataFrame)
# df = pd.read_csv('survey_data.csv',squeeze = True)
    x = add_month_yr(x)
# df =x.loc[:, ['month-yr']]
# count = df['month-yr'].value_counts()
# x = count.to_frame(name='Timestamp')
# x.index.name = 'month-yr'
# x.reset_index(inplace=True)
# print(x)

    mytype = pd.CategoricalDtype(
        categories=['Sep-2017','Jan-2018','Feb-2018','Mar-2018','Apr-2018','Sep-2018','Oct-2018','Jan-2019'],
        ordered=True
    )
    x['month-yr'] = x['month-yr'].astype(mytype)

# x.groupby('month-yr')['Timestamp'].count().to_frame().sort_index()
    return x
# df = d.assign(df)
# d.reset_index()
# x.groupby('month-yr')['Timestamp'].count().to_frame().sort_index()

# df.loc[:,'St'] = count

# pd.DataFrame(count,columns=['count'])
# df = df.set_index('month-yr')