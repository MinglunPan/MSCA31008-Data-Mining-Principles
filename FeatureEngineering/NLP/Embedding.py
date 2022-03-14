from Config import TFHUB_HANDLE_PREPROCESS, TFHUB_HANDLE_ENCODER
import tensorflow as tf
import tensorflow_hub as hub
from sklearn.feature_extraction.text import TfidfVectorizer
import tensorflow_text as text
from tqdm.notebook import tqdm


class Transformer:
    # Abstract class for transformer
    model = None
    def fit(self, text_series):
        raise NotImplementedError
    def transform(self, text_series):
        raise NotImplementedError
    def fit_transform(self, text_series):
        self.fit(text_series)
        return self.transform(text_series)

class TFIDF_Transformer(Transformer):
    def __init__(self):
        self.model = TfidfVectorizer(max_features = 15000, min_df= 3, max_df=0.5, analyzer = 'char_wb', ngram_range = (3,5))
    def fit(self, text_series):
        self.model = self.model.fit(text_series)
    def transform(self, text_series):
        return self.model.transform(text_series)

class BERT_Transformer(Transformer):
    def __init__(self):
        self.model = BERT_transformer()
    def fit(self, text_series):
        pass
    def transform(self, text_series):
        return self.model(text_series)


def BERT_transformer(tfhub_handle_encoder = TFHUB_HANDLE_ENCODER,
                    tfhub_handle_preprocess = TFHUB_HANDLE_PREPROCESS):
    text_input = tf.keras.layers.Input(shape=(), dtype=tf.string, name='text')
    preprocessing_layer = hub.KerasLayer(tfhub_handle_preprocess, name='preprocessing')
    encoder_inputs = preprocessing_layer(text_input)
    encoder = hub.KerasLayer(tfhub_handle_encoder, name='BERT_encoder')
    outputs = encoder(encoder_inputs)['pooled_output']
    return tf.keras.Model(text_input, outputs)




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
        self.fit_model(method)
        if batch_size == None:
            return self.__transform(method, text_series)
        else:
            assert isinstance(batch_size, int)
            return self.__batch_transform(method, text_series, batch_size)
    def __batch_transform(self, method, text_series, batch_size):
        result_list = []
        for i in tqdm(range(0, len(text_series)//batch_size+1)):
            batch_text = text_series.iloc[i*batch_size:(i+1)*batch_size]
            result_list.extend(self.__transform(method, batch_text))
        return result_list
    def __transform(self, method, text_series):
        return self.__transformer_dict.get(method).transform(text_series)