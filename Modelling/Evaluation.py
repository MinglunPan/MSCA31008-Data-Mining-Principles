import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score,precision_score,precision_score,recall_score,r2_score,mean_squared_error,plot_roc_curve,precision_recall_curve,ndcg_score

class Sampler:
    def holdout(self, dataset, frac, ramdon_seed):
        pass
    def Kfold(self, dataset, k_fold, random_seed):
        pass
    def replay(self, dataset, dt_column, rolling_window_size, min_train_size, max_train_size, freq):
        pass
class Metrics:
    def discretize_binary(self, continuous_series, threshold):
        return continuous_series > threshold
    def discretize(self, continuous_series, bins, labels = None):
        return pd.cut(continuous_series, bins = bins, labels = labels)
    def accuracy(self, y_true, y_pred):
        return accuracy_score(y_true,y_pred)
    def precision(self, y_true, y_pred):
        return precision_score(y_true,y_pred)
    def recall(self, y_true, y_pred):
        return recall_score(y_true,y_pred)
    def plotAUC(self, estimator, X_test, y_true):
        plot_roc_curve(estimator, X_test, y_true)
    def plotPR(self, y_true, y_pred):
        precision_recall_curve(y_true, y_pred)
    def r2(self, y_true, y_pred):
        return r2_score(y_true, y_pred)
    def rmse(self, y_true, y_pred):
        return mean_squared_error(y_true, y_pred, squared = False)
    ## By Users
    def AP_single_user(self, y_true, y_pred):
        # y_true Label should be 0,1
        y_pred = y_pred.sort()
        y_true = y_true[y_pred.index]
        return np.mean([val / (idx+1) idx, val for idx, val in enumerate(y_true.cumsum())])
    def mAP(self, *args, **kargs):
        pass
    def DCG(self, rank_scores):
        # Discounted Cumulative Gain
        return np.sum(np.divide(np.power(2, rank_scores) - 1, np.log2(np.arange(rank_scores.shape[0]) + 2)))
    def NDCG(self, y_pred_rank, y_true_rank = None):
        y_true_rank = y_true_rank or list(range(1,len(y_pred_rank+1)))
        relevance = np.ones_like(y_true_rank)

        it2rel = {it: r for it, r in zip(y_true_rank, relevance)}
        rank_scores = np.asarray([it2rel.get(it, 0.0) for it in y_pred_rank], dtype=np.float32)

        idcg = self.DCG(relevance)
        dcg = self.DCG(rank_scores)
        if dcg == 0.0:
            return 0.0
        ndcg = dcg / idcg
        return ndcg