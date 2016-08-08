# -*- coding: utf-8 -*-
import pandas as pd

def create_df(race_id):
    df = pd.read_csv('./../Data/' + race_id + '.csv', header=None)
    df = df.ix[:,:14]
    df.columns = ['rank', 'frame', 'num', 'name', 'sexAge', 'hande', 'jockey', 'time', 'diff', 'time_index', 'path', 'last', 'odds', 'fav', 'w']

    df[['sex', 'age']] = df['sexAge'].str.extract('(.)([1-9]+)')
    df[['wght','gl', 'qntty']] = df['w'].str.extract('([\d]{3})\((.?)([\d]+)\)')
    df = df[['rank', 'frame', 'num', 'sex', 'age', 'odds', 'fav', 'wght', 'gl', 'qntty']]

    dum = pd.get_dummies(df["sex"])
    size = dum/len(dum)
    if size == 2:
        dum.columns = ['f','m']
        df = pd.concat((df, dum), axis=1)
        df = df.drop("sex", axis=1)
    elif size == 3:
        dum.columns = ['f','m','g']
        df = pd.concat((df, dum), axis=1)
        df = df.drop("sex", axis=1)
    else:
        df = pd.concat((df, dum), axis=1)

    dum = pd.get_dummies(df["gl"])
    df = pd.concat((df, dum), axis=1)
    df = df.drop("gl", axis=1)

    # classify
    udf = df[df['rank'] < 6] 
    udf['target'] = 1
    ddf = df[df['rank'] > 5]
    ddf['target'] = 0
    df = pd.concat((udf, ddf), axis=0)
