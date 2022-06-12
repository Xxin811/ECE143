import pandas as pd
def split_count(x):
    '''
    This function can take the imported column as input and output the pandas dataframe.
    :param x: x is a pd.Series
    :return: pd.DataFrame object
    '''
    assert isinstance(x,pd.Series)
    # df = pd.read_csv(x,usecols=['Is there anything in particular you want to use Python for?'],squeeze = True)
    lf = x.values.tolist()
    new_lf = []
    for item in lf:
        new_lf.extend(item.split(', '))
    counts = pd.Series(new_lf).value_counts()
    df_output = pd.DataFrame(columns=['count'],data = counts)
    df_output = df_output.sort_values(by = 'count')
    return df_output


