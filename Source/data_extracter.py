import pandas as pd

def create_df(race_id):
    df = pd.read_csv('./../Data/' + race_id + '.csv', header=None)
    df = df.ix[:,:14]
    df.columns = ['rank', 'frame', 'num', 'name', 'sexAge', 'hande', 'jockey', 'time', 'diff', 'time_index', 'path', 'last', 'odds', 'fav', 'w']
    df[['sex', 'age']] = df['sexAge'].str.extract('(.)([1-9]+)')
    df[['wght','gl', 'qntty']] = df['w'].str.extract('([\d]{3})\((.?)([\d]+)\)')
    df = df[['rank', 'frame', 'num', 'sex', 'age', 'odds', 'fav', 'wght', 'gl', 'qntty']]
