import data_extracter as de
import pandas as pd
import csv
from sklearn.linear_model import SGDClassifier
ALL_PARAMS = ['frame', 'num','age','odds','fav','wght','qntty','f','m','z','p','m']
ITERATION = 10
THRESHOLD = 0.5

def predict_via_sgd(dfs, race_id):
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
        return predicts.tolist()


if __name__ == '__main__':
    '''
    MODEL1
    train_year -> all years except eval_year
    eval_year  -> one year
    '''
    df = pd.read_csv('./../Data/race_info.csv', header=None)
    years = df[9]
    # predict_via_sgd( years )
    dfs = de.create_merged_df(years)
    f = open('./../Result/sgd_default_prob.csv', 'ab')
    csvWriter = csv.writer(f)

    for race_id in years:
        print race_id
        # predict iteratly
        sum_list = predict_via_sgd(dfs,race_id)
        for i in range(0, ITERATION-1):
            list = predict_via_sgd(dfs,race_id)
            sum_list = [x+y for (x, y) in zip(sum_list, list)]
        # circulate average
        list = map(lambda x: float(x) / ITERATION, sum_list)

        # save probability
        pay_list = [race_id,]
        pay_list.extend(list)

        ## make dicision to pay or not
        # pay_list = [race_id,]
        # for index in range(1,len(list)):
        #         if list[index] >= THRESHOLD:
        #         pay_list.append(index)
        # print pay_list
        csvWriter.writerow(pay_list)
    f.close
