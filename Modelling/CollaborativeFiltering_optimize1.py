from abc import ABC
import numpy as np
from tqdm.notebook import tqdm
import pandas as pd
from scipy.sparse import rand
from sklearn.preprocessing import normalize
from sklearn.metrics.pairwise import cosine_similarity

def recommendItemCF(user_data, item_similarity_matrix, item_data, having_missing_values = False):
    if having_missing_values:
        return recommendItemCF_with_missing_values(user_data, item_similarity_matrix)
    else:
        return recommendItemCF_no_missing_values(user_data, item_similarity_matrix, item_data)

def recommendItemCF_with_missing_values(user_data, item_similarity_matrix, item_data = None):
    user_records = np.nan_to_num(np.sign(user_data),0)
    user_preference = np.nan_to_num(
        np.divide(user_data.values, user_data.sum(axis = 1).values.reshape(-1,1))
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
    return pd.DataFrame(user_results_dict).T.values

def recommendItemCF_no_missing_values(user_data, item_similarity_matrix, item_data):
    return np.dot(np.dot(user_data, item_similarity_matrix),item_data)

# Calculate the cosine similarity
def similarity_cosine(vec_x, vec_y):
    return np.dot(vec_x, vec_y) / (vec_length(vec_x) * vec_length(vec_y))
 
# Calculate the vector length
def vec_length(vector):
    return np.sqrt(np.dot(vector, vector))

def item_similarity(matrix, having_missing_values = False):
    if having_massing_values:
    # initializing matrix
        sim_matrix = np.diag(np.ones(len(matrix)))
        # looping through matrix and comparing each pair
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                # Filtering for non-missing values only
                both_filter = (matrix[i]==matrix[i]) & (matrix[j] == matrix[j])
                # Running cosine similarity on pair
                sim_matrix[i][j] = sim_matrix[j][i] = similarity_cosine(matrix[i][both_filter], matrix[j][both_filter])
    else:
        sim_matrix = cosine_similarity(matrix)
    return sim_matrix
