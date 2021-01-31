import spacy as spacy
from sklearn.feature_extraction.text import CountVectorizer

from app.ml.pipline import Extractor

spacy_en = spacy.load('en_core_web_sm')
spacy_en.remove_pipe('tagger')
spacy_en.remove_pipe('ner')
vocab = list(spacy_en.vocab.strings)


def tokenizer(text):  # create a tokenizer function
    return [tok.lemma_ for tok in spacy_en.tokenizer(text)
            if tok.text.isalpha() and len(tok.lemma_) > 1 and tok.lemma_ not in ['\ufeff1','-PRON-','-pron-']]


counters = dict(
    [(i,
      CountVectorizer(ngram_range=(1, i),
                      stop_words="english",
                      tokenizer=tokenizer,
                      # vocabulary=vocab
                      )
      )
     for i in range(1, 4)]
)
extractor = Extractor()
