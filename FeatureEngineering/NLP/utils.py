import numpy as np
import pandas as pd
import random
import torch
import os
import warnings


# Function for calculating the weighted sum of data based on a dictionary of weights
def weightedSum(data, weight_dict):
    return (data[weight_dict.keys()] * np.array(weight_dict)).sum(axis = 1)

# Function for under/oversampling
def sample_binary(data, target_col, 
                  filter_func = lambda x:x == 0, sample_method = 'undersample',
                  random_state = 42
                 ):
    filter_ = data[target_col].apply(filter_func) # Filter data for given target column and use supplied filter function/criteria 
    filter_count = filter_.value_counts().sort_values() # Get sorted value counts
    if len(filter_count) != 2: # Warning if filter counts not equal to 2
        warnings.warn("The number of class is not equal to 2")
    # undersample 大的抽小的
    # Oversample 小的抽大的（有放回）
    min_count, max_count = filter_count.values # get min and max counts
    min_class, max_class = filter_count.index # get corresponding min and max classes
    if sample_method == 'undersample':
        sample_count, sample_class = min_count,max_class # if undersampling, use min count (minority class) and set sample class as majority class -- want to reduce max class to min count samples
        replace = False
    elif sample_method == 'oversample': # if oversampling, use max count (majority class) and set sample class as minority class -- want to increase min class to max count samples
        sample_count, sample_class = max_count,min_class
        replace = True
    else: # if no sample method is provided...
        raise ValueError("No sample_method: %s"%sample_method)
    filter_ = filter_ == sample_class
    sample_df = data.loc[filter_].sample(n = sample_count, random_state = random_state, replace = replace) # undersample or oversample as determined above/from parameters
    df = pd.concat([sample_df, data.loc[-filter_]], axis = 0) # concatenate new sample df with filtered df
    return df

# Function for setting random seed
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