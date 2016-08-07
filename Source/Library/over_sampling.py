import numpy as np
class SMOTE(object):
    def __init__(self, N):
        self.N = N
        self.T = 0

    def oversampling(self, smp, cv):
        mino_idx = np.where(cv==1)[0]
        mino_smp = smp[mino_idx,:]

        mino_nn = []

        for idx in mino_idx:
            near_dist = np.array([])
            near_idx = np.zeros(nnk)
            for i in xrange(len(smp)):
                if idx != i:
                    dist = self.dist(smp[idx,:], smp[i,:])

                    if len(near_dist)<nnk:
                        tmp = near_dist.tolist()
                        tmp.append(dist)
                        near_dist = np.array(tmp)
                    elif sum(near_dist[near_dist > dist])>0:
                        near_dist[near_dist==near_dist.max()] = dist
                        near_idx[near_dist==near_dist.max()] = i
            mino_nn.append(near_idx)
        return self.create_synth( smp, mino_smp, np.array(mino_nn, dtype=np.int) )

    def dist(self, smp_1, smp_2):
        return np.sqrt( np.sum((smp_1 - smp_2)**2) )

    def create_synth(self, smp, mino_smp, mino_nn):
        self.T = len(mino_smp)
        if self.N < 100:
            self.T = int(self.N*0.01*len(mino_smp))
            self.N = 100
        self.N = int(self.N*0.01)

        rs = np.floor( np.random.uniform(size=self.T)*len(mino_smp) )

        synth = []
        for n in xrange(self.N):
            for i in rs:
                nn = int(np.random.uniform(size=1)[0]*nnk)
                dif = smp[mino_nn[i,nn],:] - mino_smp[i,:]
                gap = np.random.uniform(size=len(mino_smp[0]))
                tmp = mino_smp[i,:] + np.floor(gap*dif)
                tmp[tmp<0]=0
                synth.append(tmp)
        return synth
