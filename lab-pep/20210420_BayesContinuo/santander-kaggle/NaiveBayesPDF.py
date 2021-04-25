####
# In a pentium 7 with 12 processors and 16GB of memory
####
# For c=3
# CPU times: user 91.6 ms, sys: 144 ms, total: 235 ms
# Wall time: 48.7 s
####
# For c=0.5
# CPU times: user 80.2 ms, sys: 142 ms, total: 222 ms
# Wall time: 48.3 s
####
import numpy as np
from multiprocessing import Pool
from functools import partial
from sklearn.metrics import roc_auc_score

def get_stats(df_train, resolution = 501):
    means = df_train.drop(columns=['target', 'ID_code']).mean()
    stds = df_train.drop(columns=['target', 'ID_code']).std()
    mins = df_train.drop(columns=['target', 'ID_code']).min()
    maxs = df_train.drop(columns=['target', 'ID_code']).max()
    max_z_zcore = np.ceil(((maxs-means)/stds).max())
    min_z_zcore = np.floor(((mins-means)/stds).min())
    z_scores = np.linspace(min_z_zcore, max_z_zcore, resolution)
    return means, stds, min_z_zcore, max_z_zcore, z_scores


def likelihoods_frequency_vect(v, df_target_1, df_target_0, stds, c=3):
    # This version calculates all variables v_i in one shot
    N_interval_0 = ((df_target_0.drop(columns=['ID_code', 'target'])>v-stds/c) 
                    & (df_target_0.drop(columns=['ID_code', 'target'])<v+stds/c)).sum(axis=0)
    N_interval_1 = ((df_target_1.drop(columns=['ID_code', 'target'])>v-stds/c) 
                    & (df_target_1.drop(columns=['ID_code', 'target'])<v+stds/c)).sum(axis=0)
    return N_interval_0/(2*stds/c), N_interval_1/(2*stds/c)


def get_pdf_vect_parallel(z_scores_interval, df_target_1=None, df_target_0=None, means=None, stds=None, smoothing=1, c=3, p_1=0.1, p_0=0.9):
        # Calculates the probability density function of variable v_i for all v's
        """
        var_i: variable index
        c: smoothing for moving average
        smoothing: laplacian smoothing
        """
        # Number of variables
        N_vars = df_target_0.shape[1]-2
        
        N_0 = len(df_target_0) + p_0*smoothing*N_vars
        N_1 = len(df_target_1) + p_1*smoothing*N_vars
        ps_0 = []
        ps_1 = []
        for z in z_scores_interval:
            # Unnormalize
            v = z*stds + means
            l0, l1 = likelihoods_frequency_vect(v, df_target_1, df_target_0, stds, c=c)
            ps_0.append(l0 + p_0*smoothing)
            ps_1.append(l1 + p_1*smoothing)
        return np.array(ps_0)/N_0, np.array(ps_1)/N_1



class NaiveBayesPDF:
    def __init__(self, smoothing=1, c=3, resolution=501, N_processors=10):
        self.smoothing = smoothing
        self.c = c
        self.resolution = resolution
        self.N_processors = N_processors
        

    def __train_parallel(self, df_train, N = 10, smoothing=1, c=3, resolution=501):
        means, stds, min_z_zcore, max_z_zcore, z_scores = get_stats(df_train, resolution = resolution)
        self.means = means
        self.stds = stds
        self.min_z_zcore = min_z_zcore
        self.max_z_zcore = max_z_zcore 
        self.z_scores = z_scores
        # All the observation where target = 1
        df_target_1 = df_train[df_train['target']==1]
        # All the observation where target = 0
        df_target_0 = df_train[df_train['target']==0]
        p_1 = len(df_target_1)/len(df_train)
        p_0 = len(df_target_0)/len(df_train)

        N_paral = int(len(z_scores)/N)
        z_scores_list = []
        for i in range(N):
            z_scores_min = i*N_paral
            if i == N-1:
                z_scores_max = len(z_scores)
            else:
                z_scores_max = (i+1)*N_paral
            z_scores_list.append(list(z_scores[z_scores_min: z_scores_max]))
        likelihoods_pdfs = []
        with Pool(N) as p:
            likelihoods_pdfs = p.map(partial(get_pdf_vect_parallel, df_target_1=df_target_1, df_target_0=df_target_0, means=means, stds=stds, smoothing=smoothing, c=c, p_1=p_1, p_0=p_0), z_scores_list)
        N_vars = df_train.shape[1]-2
        likelihood_matrix_0 = np.empty((0, N_vars))
        likelihood_matrix_1 = np.empty((0, N_vars))
        for i, (l0, l1) in enumerate(likelihoods_pdfs):
            likelihood_matrix_0 = np.append(likelihood_matrix_0, l0, axis=0)
            likelihood_matrix_1 = np.append(likelihood_matrix_1, l1, axis=0)
        odds = likelihood_matrix_1/likelihood_matrix_0
        return likelihood_matrix_0, likelihood_matrix_1, odds, p_1, p_0, means, stds, z_scores

        
    def fit(self, df_train):
        self.likelihood_matrix_0_, self.likelihood_matrix_1_, self.odds_, self.p_1_, self.p_0_, self.means_, self.stds_, self.z_scores_ = \
            self.__train_parallel(df_train, N = self.N_processors, smoothing=self.smoothing, c=self.c, resolution=self.resolution)
        
    def predict(self, X, y=None):
        # Normalize
        observations_normalized = (X - self.means.values)/self.stds.values
        observations_odds = []
        for var_i in range(X.shape[1]):
            indexes = np.array(np.round(((observations_normalized[:,var_i]-self.min_z_zcore)/(self.max_z_zcore - self.min_z_zcore))*self.resolution), dtype=int)
            indexes[indexes>=self.resolution] = self.resolution - 1
            observations_odds.append(self.odds_[indexes, var_i])
        observations_odds = np.array(observations_odds).T
        log_odds = np.sum(np.log(observations_odds), axis=1) + np.log(self.p_1_/self.p_0_)
        prod_odds = np.exp(log_odds)
        auc = None
        acc = None
        if y is not None:
            auc = roc_auc_score(y, prod_odds)
            acc = (y == (prod_odds>=1)).sum()/len(y)

        return observations_normalized, observations_odds, log_odds, prod_odds, prod_odds/(1 + prod_odds), auc, acc