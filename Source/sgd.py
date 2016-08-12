import data_extracter as de
import pandas as pd
import csv
from sklearn.linear_model import SGDClassifier
ALL_PARAMS = ['frame', 'num','age','odds','fav','wght','qntty','f','m','z','p','m']

def predict_via_sgd(years):
    dfs = de.create_merged_df(years)
    f = open('./../Result/sgd_default.csv', 'ab')
    csvWriter = csv.writer(f)

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
        list = [race_id, ]
        list.append(predicts.tolist())
        csvWriter.writerow(list)
    f.close


if __name__ == '__main__':
    '''
    MODEL1
    train_year -> all years except eval_year
    eval_year  -> one year
    '''
    df = pd.read_csv('./../Data/race_info.csv', header=None)
    years = df[9]
    predict_via_sgd( years )
