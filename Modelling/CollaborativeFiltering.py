from abc import ABC
import numpy as np
from tqdm.notebook import tqdm
import pandas as pd

def similarity_cosine(vec_x, vec_y):
    return np.dot(vec_x, vec_y) / (vec_length(vec_x) * vec_length(vec_y))
def vec_length(vector):
    return np.sqrt(np.dot(vector, vector))
def similarity_pearson(vec_x, vec_y):
    vec_x_normalized = vec_x - vec_x.mean()
    vec_y_normalized = vec_y - vec_y.mean()
    return np.dot(vec_x_normalized, vec_y_normalized) / (vec_length(vec_x_normalized) * vec_length(vec_y_normalized))
def recommendItemCF(data,user_data, item_similarity_matrix, item_columns):
    
    user_records = np.sign(user_data[item_columns].values)
    user_preference = np.divide(user_data[item_columns], 
                                user_data[item_columns].sum(axis = 1).to_frame()).fillna(0).values # Normalized
    user_results_dict = {}
    for i,idx in tqdm(enumerate(user_data.index)):
        item_list = user_records[i]
        item_weights = user_preference[i]
        user_results_dict[idx] = pd.Series(np.sum(item_list * item_similarity_matrix * item_weights, axis = 0))
    return pd.DataFrame({key:value.to_dict() for key,value in user_results_dict.items()})




def item_similarity(matrix):
    sim_matrix = np.diag(np.ones(len(matrix)))
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            sim_matrix[i][j] = sim_matrix[j][i] = similarity_pearson(matrix[i], matrix[j])
    return sim_matrix