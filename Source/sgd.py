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

def predict_via_sgd(years):
    dfs = de.create_merged_df(years)

    for race_id in years:
        print race_id
        evalt_df = dfs[dfs['race_id'] == race_id]
        train_df = dfs[dfs['race_id'] != race_id]

        X = train_df[ALL_PARAMS]
        y = train_df[['target']]

        clf = SGDClassifier(loss="log", penalty="l2")
        clf.fit(X, y)

        eX = evalt_df[ALL_PARAMS]
        # ey = evalt_df[['target']]

        predicts = clf.predict(eX)
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
    predict_via_sgd( years )
