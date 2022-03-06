import re
from bs4 import BeautifulSoup
from functools import lru_cache
import emoji

SIMILAR_WORDS_PATTERNS = {
    ' american ':
        [
            'amerikan'
        ],
    ' adolf ':
        [
            'adolf'
        ],
    ' hitler ':
        [
            'hitler'
        ],
    ' fuck':
        [
            '(f)(u|[^a-z0-9 ])(c|[^a-z0-9 ])(k|[^a-z0-9 ])([^ ])*',
            '(f)([^a-z]*)(u)([^a-z]*)(c)([^a-z]*)(k)',
            ' f[!@#\$%\^\&\*]*u[!@#\$%\^&\*]*k', 'f u u c',
            '(f)(c|[^a-z ])(u|[^a-z ])(k)', r'f\*',
            'feck ', ' fux ', 'f\*\*', 
            'f\-ing', 'f\.u\.', 'f###', ' fu ', 'f@ck', 'f u c k', 'f uck', 'f ck'
        ],
    ' ass ':
        [
            '[^a-z]ass ', '[^a-z]azz ', 'arrse', ' arse ', '@\$\$'
                                                           '[^a-z]anus', ' a\*s\*s', '[^a-z]ass[^a-z ]',
            'a[@#\$%\^&\*][@#\$%\^&\*]', '[^a-z]anal ', 'a s s'
        ],
    ' ass hole ':
        [
            ' a[s|z]*wipe', 'a[s|z]*[w]*h[o|0]+[l]*e', '@\$\$hole'
        ],
    ' bitch ':
        [
            'b[w]*i[t]*ch', 'b!tch',
            'bi\+ch', 'b!\+ch', '(b)([^a-z]*)(i)([^a-z]*)(t)([^a-z]*)(c)([^a-z]*)(h)',
            'biatch', 'bi\*\*h', 'bytch', 'b i t c h'
        ],
    ' bastard ':
        [
            'ba[s|z]+t[e|a]+rd'
        ],
    ' trans gender':
        [
            'transgender'
        ],
    ' gay ':
        [
            'gay'
        ],
    ' cock ':
        [
            '[^a-z]cock', 'c0ck', '[^a-z]cok ', 'c0k', '[^a-z]cok[^aeiou]', ' cawk',
            '(c)([^a-z ])(o)([^a-z ]*)(c)([^a-z ]*)(k)', 'c o c k'
        ],
    ' dick ':
        [
            ' dick[^aeiou]', 'deek', 'd i c k'
        ],
    ' suck ':
        [
            'sucker', '(s)([^a-z ]*)(u)([^a-z ]*)(c)([^a-z ]*)(k)', 'sucks', '5uck', 's u c k'
        ],
    ' cunt ':
        [
            'cunt', 'c u n t'
        ],
    ' bull shit ':
        [
            'bullsh\*t', 'bull\$hit'
        ],
    ' homo sex ual':
        [
            'homosexual'
        ],
    ' jerk ':
        [
            'jerk'
        ],
    ' idiot ':
        [
            'i[d]+io[t]+', '(i)([^a-z ]*)(d)([^a-z ]*)(i)([^a-z ]*)(o)([^a-z ]*)(t)', 'idiots'
                                                                                      'i d i o t'
        ],
    ' dumb ':
        [
            '(d)([^a-z ]*)(u)([^a-z ]*)(m)([^a-z ]*)(b)'
        ],
    ' shit ':
        [
            'shitty', '(s)([^a-z ]*)(h)([^a-z ]*)(i)([^a-z ]*)(t)', 'shite', '\$hit', 's h i t'
        ],
    ' shit hole ':
        [
            'shythole'
        ],
    ' retard ':
        [
            'returd', 'retad', 'retard', 'wiktard', 'wikitud'
        ],
    ' rape ':
        [
            ' raped'
        ],
    ' dumb ass':
        [
            'dumbass', 'dubass'
        ],
    ' ass head':
        [
            'butthead'
        ],
    ' sex ':
        [
            'sexy', 's3x', 'sexuality'
        ],
    ' nigger ':
        [
            'nigger', 'ni[g]+a', ' nigr ', 'negrito', 'niguh', 'n3gr', 'n i g g e r'
        ],
    ' shut the fuck up':
        [
            'stfu'
        ],
    ' pussy ':
        [
            'pussy[^c]', 'pusy', 'pussi[^l]', 'pusses'
        ],
    ' faggot ':
        [
            'faggot', ' fa[g]+[s]*[^a-z ]', 'fagot', 'f a g g o t', 'faggit',
            '(f)([^a-z ]*)(a)([^a-z ]*)([g]+)([^a-z ]*)(o)([^a-z ]*)(t)', 'fau[g]+ot', 'fae[g]+ot',
        ],
    ' mother fucker':
        [
            ' motha ', ' motha f', ' mother f', 'motherucker',
        ],
    ' whore ':
        [
            'wh\*\*\*', 'w h o r e'
        ],
}

class TextCleaner:
    def __init__(self, procedure):
        self.action_dict = {
            'remove':TextRemover(),
            'modify':TextModifier()
        }
        self.__procedure_func_list = []

        self.procedure = procedure

    @property
    def procedure(self):
        return self.__procedure
    @procedure.setter
    def procedure(self, procedure):
        self.__procedure_func_list = []
        for action, obj in procedure:
            self.__procedure_func_list.append(self.action_dict[action][obj])
        return self.__procedure_func_list  
    def clean(self, text):
        for func in self.__procedure_func_list:
            try:
                text = func(text)
            except Exception as e:
                print(e.msg, func)
                raise e
        return text

class TextModifier:
    def __init__(self):
        self.__func_dict = {
            "Emoji":self._replace_emoji,
            'Lower':self._lower,
            'SimilarWords':self._replace_similar_words,
        }
    def __getitem__(self, key):
        return self.__func_dict[key]
    def _replace_emoji(self, text):
        text = emoji.demojize(text)
        return text
    def _lower(self, text):
        return text.lower()
    def _replace_similar_words(self, text, similar_words = SIMILAR_WORDS_PATTERNS):
        for target, patterns in similar_words.items():
            for pat in patterns:
                text = re.sub(pat, target, text)
        return text
    
class TextRemover:
    def __init__(self):
        self.__func_dict = {
            'HTMLTags':self._removeHTMLTags,
            'URL':self._removeURL,
            'Emoji':self._removeEmoji,
            'SpecialCharacters':self._removeSpecialCharacters,
            'ExtraSpaces':self._removeBegingEndSpace,
            'BegingEndSpace':self._removeBegingEndSpace,
            }
    def __getitem__(self, key):
        return self.__func_dict[key]
    def _removeHTMLTags(self, text):
        soup = BeautifulSoup(text, 'lxml') #Removes HTML tags
        text = soup.get_text()
        return text
    def _removeURL(self, text):
        template = re.compile(r'https?://\S+|www\.\S+') #Removes website links
        text = template.sub(r'', text)
        return text
    def _removeEmoji(self, text):
        emoji_pattern = re.compile("["
                                u"\U0001F600-\U0001F64F"  # emoticons
                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                u"\U00002702-\U000027B0"
                                u"\U000024C2-\U0001F251"
                                "]+", flags=re.UNICODE)
        text = emoji_pattern.sub(r'', text)
        return text
    def _removeSpecialCharacters(self, text):
        text = re.sub(r"[^a-zA-Z\d]", " ", text)
        return text
    def _removeExtraSpaces(self, text):
        text = re.sub('\s+', ' ', text) #Remove Extra Spaces
        return text #Remove Extra Spaces
    def _removeBegingEndSpace(self, text):
        return text.strip()


