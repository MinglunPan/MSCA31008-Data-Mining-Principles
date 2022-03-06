DEFAULT_CLEAN_PROCEDURE = (
    ('modify','Emoji'),
    ('modify','Lower'),
    ('modify','SimilarWords'),
    ('remove','HTMLTags'),
    ('remove','URL'),
    ('remove','Emoji'),
    ('remove','SpecialCharacters'),
    ('remove','ExtraSpaces'),
    ('remove','BegingEndSpace'),
)

DATA_PATH = '/home/adrian/Projects/Competition/data/kaggle-toxic-comments-2021'

TFHUB_HANDLE_PREPROCESS = 'https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3'
TFHUB_HANDLE_ENCODER = 'https://tfhub.dev/tensorflow/small_bert/bert_en_uncased_L-12_H-256_A-4/2'


