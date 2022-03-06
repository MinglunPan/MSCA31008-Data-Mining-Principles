import numpy as np
import pandas as pd
import random
import torch
import os
import warnings



def weightedSum(data, weight_dict):
    return (data[weight_dict.keys()] * np.array(weight_dict)).sum(axis = 1)


def sample_binary(data, target_col, 
                  filter_func = lambda x:x == 0, sample_method = 'undersample',
                  random_state = 42
                 ):
    filter_ = data[target_col].apply(filter_func)
    filter_count = filter_.value_counts().sort_values()
    if len(filter_count) != 2:
        warnings.warn("The number of class is not equal to 2")
    # undersample 大的抽小的
    # Oversample 小的抽大的（有放回）
    min_count, max_count = filter_count.values
    min_class, max_class = filter_count.index
    if sample_method == 'undersample':
        sample_count, sample_class = min_count,max_class
        replace = False
    elif sample_method == 'oversample':
        sample_count, sample_class = max_count,min_class
        replace = True
    else:
        raise ValueError("No sample_method: %s"%sample_method)
    filter_ = filter_ == sample_class
    sample_df = data.loc[filter_].sample(n = sample_count, random_state = random_state, replace = replace)
    df = pd.concat([sample_df, data.loc[-filter_]], axis = 0)
    return df


def set_seed(seed = 42):
    '''Sets the seed of the entire notebook so results are the same every time we run.
    This is for REPRODUCIBILITY.'''
    np.random.seed(seed)
    random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    # When running on the CuDNN backend, two further options must be set
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    # Set a fixed value for the hash seed
    os.environ['PYTHONHASHSEED'] = str(seed)