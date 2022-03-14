from Config import TFHUB_HANDLE_PREPROCESS, TFHUB_HANDLE_ENCODER
import tensorflow as tf
import tensorflow_hub as hub
from sklearn.feature_extraction.text import TfidfVectorizer
import tensorflow_text as text
from tqdm.notebook import tqdm


class Transformer:
    # Abstract class for transformer
    model = None
    # Fit function
    def fit(self, text_series):
        raise NotImplementedError
    # Transform function
    def transform(self, text_series):
        raise NotImplementedError
    # Fit/transform function
    def fit_transform(self, text_series):
        self.fit(text_series)
        return self.transform(text_series)

# TFIDF transformer class
class TFIDF_Transformer(Transformer):
    def __init__(self): # Initialize model with default parameters
        self.model = TfidfVectorizer(max_features = 15000, min_df= 3, max_df=0.5, analyzer = 'char_wb', ngram_range = (3,5))
    def fit(self, text_series): # Fit TFIDF
        self.model = self.model.fit(text_series)
    def transform(self, text_series): # Transform TFIDF
        return self.model.transform(text_series)

# BERT transformer class
class BERT_Transformer(Transformer):
    def __init__(self):
        self.model = BERT_transformer() # Initialize model
    def fit(self, text_series): # Fit BERT
        pass
    def transform(self, text_series): # Transform BERT
        return self.model(text_series)

# BERT transformer function
def BERT_transformer(tfhub_handle_encoder = TFHUB_HANDLE_ENCODER,
                    tfhub_handle_preprocess = TFHUB_HANDLE_PREPROCESS):
    text_input = tf.keras.layers.Input(shape=(), dtype=tf.string, name='text') # Create input layer for text
    preprocessing_layer = hub.KerasLayer(tfhub_handle_preprocess, name='preprocessing') # Create preprocesing layer
    encoder_inputs = preprocessing_layer(text_input) # Get encoder inputs by passing text through preprocessing layer
    encoder = hub.KerasLayer(tfhub_handle_encoder, name='BERT_encoder') # create encoder layer
    outputs = encoder(encoder_inputs)['pooled_output'] # get outputs by encoding processed texts
    return tf.keras.Model(text_input, outputs) # return Keras model



# Embedding class
class Embedding:
    # Administrator to mnanage different transformers and 
    # provide a integrated class to manipulate the transformers
    TRANSFORMER_DICT = {
        "TFIDF":TFIDF_Transformer,
        "BERT":BERT_Transformer
    }

    def __init__(self):
        self.text_series = None
        self.__transformer_dict = None
        self.__fit_dict = None
        self.init(None)
    def init(self, text_series):
        self.text_series = text_series
        self.__transformer_dict = {key:None for key in self.TRANSFORMER_DICT.keys()}
        self.__fit_dict = {key:False for key in self.__transformer_dict.keys()}
    def fit(self, text_series):
        # pass the data to the embedding class
        # but not actually fit any specific model
        # just save a pointer
        self.init(text_series)
    def fit_model(self, method):
        # specify the model to fit
        if not self.isFit(method):
            self.__transformer_dict[method] = self.TRANSFORMER_DICT.get(method)()
            self.__transformer_dict[method].fit(self.text_series)
            self.__fit_dict[method] = True
    def isFit(self, method):
        # check whether model is fitted
        assert method in self.__fit_dict
        return self.__fit_dict.get(method)
    def transform(self, method, text_series, batch_size = None):
        # transform data
        self.fit_model(method)
        if batch_size == None:
            return self.__transform(method, text_series)
        else:
            assert isinstance(batch_size, int)
            return self.__batch_transform(method, text_series, batch_size)
    def __batch_transform(self, method, text_series, batch_size):
        # transform data in batches
        result_list = []
        for i in tqdm(range(0, len(text_series)//batch_size+1)):
            batch_text = text_series.iloc[i*batch_size:(i+1)*batch_size]
            result_list.extend(self.__transform(method, batch_text))
        return result_list
    def __transform(self, method, text_series):
        return self.__transformer_dict.get(method).transform(text_series)