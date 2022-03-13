from abc import ABC
import numpy as np
from tqdm.notebook import tqdm
import pandas as pd
from scipy.sparse import rand
from sklearn.preprocessing import normalize
from sklearn.metrics.pairwise import cosine_similarity

def recommendItemCF_o2(user_data, item_similarity_matrix, item_columns):
    user_data_index = user_data.index.to_numpy()
    user_data = user_data.to_numpy()
    user_records = np.sign(user_data[item_columns])
    user_preference = np.divide(user_data, user_data.sum(axis = 1))
    user_results_dict = {}
    for i,idx in tqdm(enumerate(user_data_index)):
        item_list = user_records[i]
        item_weights = user_preference[i]
        user_results_dict[idx] = dict(enumerate(np.sum(item_list * item_similarity_matrix * item_weights, axis = 0).flatten(), 1))

    return pd.DataFrame(user_results_dict)

def item_similarity_o(matrix):
    return cosine_similarity(matrix)
