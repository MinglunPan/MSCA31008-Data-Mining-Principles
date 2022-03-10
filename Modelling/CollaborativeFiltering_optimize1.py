from abc import ABC
import numpy as np
from tqdm.notebook import tqdm
import pandas as pd
from scipy.sparse import rand
from sklearn.preprocessing import normalize
from sklearn.metrics.pairwise import cosine_similarity

def recommendItemCF_o2(user_data, item_similarity_matrix, item_columns):
    user_records = np.nan_to_num(np.sign(user_data[item_columns]),0)
    user_preference = np.nan_to_num(
        np.divide(user_data[item_columns].values, user_data[item_columns].sum(axis = 1).values.reshape(-1,1))
        ,0)
    user_results_dict = {}
    for i,idx in tqdm(enumerate(user_data.index)):
        item_list = user_records[i]
        item_weights = user_preference[i]
        user_results_dict[idx] = dict(
            enumerate(
                np.sum(item_list * item_similarity_matrix * item_weights, axis = 1),
                1
            )
        )

    return pd.DataFrame(user_results_dict).T


def item_similarity_o2(matrix):
    return cosine_similarity(matrix)

if __name__ == '__main__':
    user_data = np.random.random_integers(0, 5, (10,5))
    user_data = pd.DataFrame(user_data)

    # What we expect here is the similarities of items,
    # thus we transpose the user matrix
    sim_mat = item_similarity_o2(user_data.T) 
    recommendItemCF_o2(user_data, sim_mat, user_data.columns)
