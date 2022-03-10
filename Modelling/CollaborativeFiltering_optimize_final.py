import numpy as np
from tqdm.notebook import tqdm
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def recommendItemCF(user_data, item_columns):
    user_records = np.sign(user_data[item_columns])
    user_preference = np.divide(user_data[item_columns], 
                                user_data[item_columns].sum(axis = 1).to_frame()).fillna(0).values
    
    if user_data.shape[0] == user_data.shape[1]:
        return pd.DataFrame(np.einsum("ij,jk,ij->ji", user_records, cosine_similarity(user_data), user_preference))
    else:
        return pd.DataFrame(np.einsum("ij,jk,ij->ji", user_records.T, cosine_similarity(user_data).T, user_preference.T))
