import pandas as pd

from utils import weightedSum
from TextCleaner import TextCleaner
from Config import DEFAULT_CLEAN_PROCEDURE
# from tqdm import tqdm_notebook

from tqdm.notebook import tqdm_notebook as tqdm
tqdm.pandas()

class DatasetProcessor:
    def __init__(self, procedures):
        self.procedures = procedures
    def set_target(self, data, response_col = None, average_weights_dict = None, y_col = 'y'):
        assert (response_col == None)^(average_weights_dict == None)
        if average_weights_dict != None: 
            assert isinstance(average_weights_dict, dict)
            return weightedSum(data, average_weights_dict)
        if response_col != None: 
            assert isinstance(response_col, str)
            assert response_col in data.columns
            return data[response_col]
    def clean_text(self, text_series, show_progress = True):
        assert text_series.dtype == 'O'
        cleaner = TextCleaner(self.procedures)
        if show_progress:
            return text_series.progress_apply(cleaner.clean)
        else:
            return text_series.apply(cleaner.clean)
    