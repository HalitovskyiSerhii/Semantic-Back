import logging

import wikipedia as wp
from wikipedia import PageError, WikipediaException


def wp_search(key_word):
    try:
        res = wp.search(key_word)
        disambiguation = len(res) > 1
        print(res)
        urls = []
        for title in res[:5]:
            try:
                page = wp.page(title=title)
                urls.append((title, page.url))
            except (PageError, WikipediaException) as ex:
                logging.error(str(ex))

        return {"key_word": key_word, "urls": list(urls), "disambiguation": disambiguation}
    except Exception as ex:
        logging.error(str(ex))
