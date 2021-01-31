from app.dal.wiki import wp_search
from app.ml import extractor, counters
from extensions import es_util


class ExtractorService(object):

    def extract(self, text, words, top):
        return extractor.fit(text, counters[words], top)


class ElasticService(object):
    def __init__(self):
        self.rep = es_util.repository

    def save(self, text, key_phrases):
        self.rep.save({"type": "doc", "body": text, "key_phrases": key_phrases})


class WikiService(object):

    def search(self, key_phrases):
        res = []
        for key_phrase in key_phrases:
            pages = wp_search(key_phrase)
            if pages:
                res.append(pages)

        return res