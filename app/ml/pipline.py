from sentence_transformers import SentenceTransformer
from app.ml.utils import mmr


class Extractor(object):

    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.model = SentenceTransformer('distilbert-base-nli-mean-tokens')

    def fit(self, doc, counter, top_n=3):
        # Extract candidate words/phrases
        counter.fit([doc])
        candidates = counter.get_feature_names()

        doc_embedding = self.model.encode([doc], batch_size=1)
        bs = 128 if len(candidates) > 128 else len(candidates)
        candidate_embeddings = self.model.encode(candidates, batch_size=bs)

        keywords = mmr(doc_embedding, candidate_embeddings, candidates, top_n, 0.4)

        self.clean_keywords(keywords)
        print(keywords)

        return keywords

    def clean_keywords(self, keywords):
        for k, keyword in enumerate(keywords):
            print(keyword)
            lemmas: list = self.tokenizer(keyword, True)
            words: list = self.tokenizer(keyword, False)
            for i, lemma in enumerate(lemmas[:]):
                if lemmas.count(lemma) > 1:
                    del lemmas[i]
                    del words[i]
            keywords[k] = ' '.join(words)
