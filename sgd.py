import version
import merge_metrics_more as mmm
import evaluation as evl
import pandas as  pd
from sklearn.linear_model import SGDClassifier



def predict_via_sgd(curr_ver):
    X = curr_df[nml_prm]
    y = curr_df[['fault']]
    # print X
    # print y

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

for i in range(0,50):
    predict_via_sgd('4.4.0')
