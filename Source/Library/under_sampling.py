def undersampling(imp_info, cv, m):
    # minority data
    minodata = imp_info[np.where(cv==1)[0]]

    # majority data
    majodata = imp_info[np.where(cv==0)[0]]

    # kmeans2でクラスタリング
    whitened = whiten(imp_info) # 正規化（各軸の分散を一致させる）
    centroid, label = kmeans2(whitened, k=3) # kmeans2
    C1 = []; C2 = []; C3 = []; # クラスタ保存用
    C1_cv = []; C2_cv = []; C3_cv = []
    for i in xrange(len(imp_info)):
        if label[i] == 0:
            C1 += [whitened[i]]
            C1_cv.append(cv[i])
        elif label[i] == 1:
            C2 += [whitened[i]]
            C2_cv.append(cv[i])
        elif label[i] == 2:
            C3 += [whitened[i]]
            C3_cv.append(cv[i])

    # numpy形式の方が扱いやすいため変換
    C1 = np.array(C1); C2 = np.array(C2); C3 = np.array(C3)
    C1_cv = np.array(C1_cv); C2_cv = np.array(C2_cv); C3_cv = np.array(C3_cv);

    # 各クラスの少数派データの数
    C1_Nmajo = sum(1*(C1_cv==0)); C2_Nmajo = sum(1*(C2_cv==0)); C3_Nmajo = sum(1*(C3_cv==0))

    # 各クラスの多数派データの数
    C1_Nmino = sum(1*(C1_cv==1)); C2_Nmino = sum(1*(C2_cv==1)); C3_Nmino = sum(1*(C3_cv==1))
    t_Nmino = C1_Nmino + C2_Nmino + C3_Nmino

    # 分母に0が出る可能性があるので1をプラスしておく
    C1_MAperMI = float(C1_Nmajo)/(C1_Nmino+1); C2_MAperMI = float(C2_Nmajo)/(C2_Nmino+1); C3_MAperMI = float(C3_Nmajo)/(C3_Nmino+1);

    t_MAperMI = C1_MAperMI + C2_MAperMI + C3_MAperMI

    under_C1_Nmajo = int(m*t_Nmino*C1_MAperMI/t_MAperMI)
    under_C2_Nmajo = int(m*t_Nmino*C2_MAperMI/t_MAperMI)
    under_C3_Nmajo = int(m*t_Nmino*C3_MAperMI/t_MAperMI)
    t_under_Nmajo = under_C1_Nmajo + under_C2_Nmajo + under_C3_Nmajo

#    draw(majodata, label)

    # 各グループで多数派と少数派が同数になるようにデータを削除
    C1 = C1[np.where(C1_cv==0),:][0]
    random.shuffle(C1)
    C1 = np.array(C1)
    C1 = C1[:under_C1_Nmajo,:]
    C2 = C2[np.where(C2_cv==0),:][0]
    random.shuffle(C2)
    C2 = np.array(C2)
    C2 = C2[:under_C2_Nmajo,:]
    C3 = C3[np.where(C3_cv==0),:][0]
    random.shuffle(C3)
    C3 = np.array(C3)
    C3 = C3[:under_C3_Nmajo,:]

    cv_0 = np.zeros(t_under_Nmajo); cv_1 = np.ones(len(minodata))
    cv_d = np.hstack((cv_0, cv_1))

    info = np.vstack((C1, C2, C3, minodata))

    return cv_d, info
