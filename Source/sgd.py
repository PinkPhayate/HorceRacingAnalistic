import data_extracter as de
import pandas as pd
from sklearn.linear_model import SGDClassifier
ALL_PARAMS = ['frame', 'num','age','odds','fav','wght','qntty','f','m','z','p','m']

def get_train_years(eval_year):
    df = pd.read_csv('./../Data/race_info.csv', header=None)
    years = df[9]
    train_years = []
    for year in years:
        if year != eval_year:
            train_years.append(year)
    return train_years

def predict_via_sgd(eval_year, train_years):
    # dfs = pd.DataFrame([])
    # for year in train_years:
    #     df = de.create_df(str(year))
    #     dfs = pd.concat([dfs, df])
    dfs = de.create_merged_df(train_years)
    # dfs = de.create_merged_df(eval_year, train_years)
    dfs = dfs.dropna(axis=0)
    X = dfs[ALL_PARAMS]
    y = dfs[['target']]

    clf = SGDClassifier(loss="log", penalty="l2")
    clf.fit(X, y)

    df = de.create_df(str(eval_year))
    predicts = clf.predict(df)
    print predicts

    # dict = evl.circulate_fvalue(next_df, nml_prm, predicts)
    # print dict

if __name__ == '__main__':
    '''
    MODEL1
    train_year -> all years except eval_year
    eval_year  -> one year
    '''
    df = pd.read_csv('./../Data/race_info.csv', header=None)
    years = df[9]
    print 'get data'
    for eval_year in years:
        print eval_year
        train_years = get_train_years(eval_year)
        predict_via_sgd(eval_year, train_years)
        break
