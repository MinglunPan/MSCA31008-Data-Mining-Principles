import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score,precision_score,precision_score,recall_score,r2_score,mean_squared_error,plot_roc_curve,precision_recall_curve,ndcg_score

# Class for creating holdout set, kfold cv, replay functions
class Sampler:
    def holdout(self, dataset, frac, ramdon_seed):
        pass
    def Kfold(self, dataset, k_fold, random_seed):
        pass
    def replay(self, dataset, dt_column, rolling_window_size, min_train_size, max_train_size, freq):
        pass
# Metric class
class Metrics:
    # Discretize binary
    def discretize_binary(self, continuous_series, threshold): 
        return continuous_series > threshold
    # Discretize
    def discretize(self, continuous_series, bins, labels = None):
        return pd.cut(continuous_series, bins = bins, labels = labels)
    # Accuracy measure
    def accuracy(self, y_true, y_pred):
        return accuracy_score(y_true,y_pred)
    # Precision measure
    def precision(self, y_true, y_pred):
        return precision_score(y_true,y_pred)
    # Recall measure
    def recall(self, y_true, y_pred):
        return recall_score(y_true,y_pred)
    # Plot ROC curve
    def plotAUC(self, estimator, X_test, y_true):
        plot_roc_curve(estimator, X_test, y_true)
    # Plot precision-recall curve
    def plotPR(self, y_true, y_pred):
        precision_recall_curve(y_true, y_pred)
    # R^2 measure
    def r2(self, y_true, y_pred):
        return r2_score(y_true, y_pred)
    # RMSE measure
    def rmse(self, y_true, y_pred):
        return mean_squared_error(y_true, y_pred, squared = False)
    ## By Users
    # Average precision for single user
    def AP_single_user(self, y_true, y_pred):
        # y_true Label should be 0,1
        y_pred = y_pred.sort()
        y_true = y_true[y_pred.index]
        return np.mean([val / (idx+1) idx, val for idx, val in enumerate(y_true.cumsum())])
    # Mean average precision
    def mAP(self, *args, **kargs):
        pass
    # Discounted cumulative gain
    def DCG(self, rank_scores):
        return np.sum(np.divide(np.power(2, rank_scores) - 1, np.log2(np.arange(rank_scores.shape[0]) + 2)))
    # Normalized discounted cumulative gain
    def NDCG(self, y_pred_rank, y_true_rank):
        return ndcg_score(y_true_rank, y_pred_rank)