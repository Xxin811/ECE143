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

def count_month_yr(x):
    '''
    This function is used to create the dataframe using the new column month-yr,
    :param x: a dataframe
    :return: a dataframe
    '''

    assert isinstance(x,pd.DataFrame)
    # df = pd.read_csv('survey_data.csv',squeeze = True)
    x = add_month_yr(x)
    df =x.loc[:, ['month-yr']]

    # df = df.sort_values(by="month-yr")
    count = df['month-yr'].value_counts()
    x = count.to_frame(name='Timestamp')
    x.index.name = 'month-yr'
    return x
# df = d.assign(df)
# d.reset_index()
# df2 = df2.set_index('month-yr')

# df.loc[:,'St'] = count

# pd.DataFrame(count,columns=['count'])
# df = df.set_index('month-yr')

# # counts = pd.Series(df).value_counts()
# # df_output = pd.DataFrame(columns=['count'],data = counts)
#
# # df = df.loc[:, ['month-yr']]
# #     return x
# print(df)