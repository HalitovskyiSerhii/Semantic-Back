import logging

import wikipedia as wp
from wikipedia import PageError, DisambiguationError, WikipediaPage


def wp_search(key_word):
    disambiguation = False
    urls = []

    try:
        wp.page(title=key_word, auto_suggest=False)
    except DisambiguationError as er:
        for title in er.options[:3]:
            page = wp.page(title=title, auto_suggest=False)
            urls.append((title, page.url))
        disambiguation = True
        return {"key_word": key_word, "urls": list(urls), "disambiguation": disambiguation}

    except PageError as ex:
        logging.error(f"Page doesn't exists: {key_word}")

    if not urls:
        res = wp.search(key_word, results=5)
        for title in res:
            page = wp.page(title=title, auto_suggest=False)
            if key_word in page.title.lower():
                urls.append((page.title, page.url))
                break

    return {"key_word": key_word, "urls": list(urls), "disambiguation": disambiguation}
