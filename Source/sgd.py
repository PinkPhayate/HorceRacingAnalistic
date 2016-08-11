import data_extracter as de
import evaluation as evl
import pandas as  pd
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




# def predict_via_sgd(eval_year):
def predict_via_sgd(eval_year, train_years):
    dfs = pd.Dataframe([])
    for year in train_years:
        df = de.create_df(year)
        dfs = pd.concat([dfs, df])
    X = dfs[ALL_PARAMS]
    y = dfs[['target']]

    clf = SGDClassifier(loss="log", penalty="l2")
    clf.fit(X, y)
    SGDClassifier(alpha=0.0001, average=False, class_weight=None, epsilon=0.1,
           eta0=0.0, fit_intercept=True, l1_ratio=0.15,
           learning_rate='optimal', loss='hinge', n_iter=5, n_jobs=1,
           penalty='l2', power_t=0.5, random_state=None, shuffle=True,
           verbose=0, warm_start=False)
    next_ver = version.get_next_version(curr_ver)
    next_df = mmm.create_df(next_ver)
    metircs = next_df[nml_prm]
    predicts = clf.predict(metircs)
    # print predicts



        dict = evl.circulate_fvalue(next_df, nml_prm, predicts)
        print dict

if __name__ == '__main__':
    '''
    MODEL1
    train_year->all years except eval_year
    eval_year-> one year
    '''
    df = pd.read_csv('./../Data/race_info.csv', header=None)
    years = df[9]
    for eval_year in years:
        train_years = get_train_years(eval_year)
        predict_via_sgd(eval_year, train_years)
