from abc import ABC
import numpy as np
from tqdm.notebook import tqdm
import pandas as pd
from scipy.sparse import rand
from sklearn.preprocessing import normalize
from sklearn.metrics.pairwise import cosine_similarity

def recommendItemCF_o(user_data, item_similarity_matrix, item_columns):
    user_records = np.sign(user_data[item_columns])
    user_preference = np.divide(user_data[item_columns], 
                                user_data[item_columns].sum(axis = 1).to_frame()).fillna(0).values #this line gives issues if dimensions are off -- can transpose?
    user_results_dict = {}
    for i,idx in tqdm(enumerate(user_data.index)):
        item_list = user_records[i]
        item_weights = user_preference[i]
        user_results_dict[idx] = dict(enumerate(np.sum(item_list.values * item_similarity_matrix * item_weights, axis = 0).flatten(), 1)) #this line gives issues if dimensions are off -- can reshape? 

    return pd.DataFrame(user_results_dict)


def item_similarity_o(matrix):
    return cosine_similarity(matrix)
