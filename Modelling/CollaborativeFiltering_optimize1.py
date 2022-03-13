from abc import ABC
import numpy as np
from tqdm.notebook import tqdm
import pandas as pd
from scipy.sparse import rand
from sklearn.preprocessing import normalize
from sklearn.metrics.pairwise import cosine_similarity


def recommendItemCF(user_data, item_similarity_matrix, item_columns):
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

# Calculate the cosine similarity
def similarity_cosine(vec_x, vec_y):
    return np.dot(vec_x, vec_y) / (vec_length(vec_x) * vec_length(vec_y))
 
# Calculate the vector length
def vec_length(vector):
    return np.sqrt(np.dot(vector, vector))

def item_similarity(matrix):
    # initializing matrix
    sim_matrix = np.diag(np.ones(len(matrix)))
    # looping through matrix and comparing each pair
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            # Filtering for non-missing values only
            i_filter = np.where(matrix.iloc[i].values == matrix.iloc[i].values)
            j_filter = np.where(matrix.iloc[j].values == matrix.iloc[j].values)
            both_filter = np.intersect1d(i_filter, j_filter)
            # Running cosine similarity on pair
            sim_matrix[i][j] = sim_matrix[j][i] = similarity_cosine(matrix.iloc[i].values[both_filter], matrix.iloc[j].values[both_filter])
    return sim_matrix
