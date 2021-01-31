from flask import Blueprint, request, json, abort

from app.api.services import ExtractorService, ElasticService, WikiService

api = Blueprint('api', __name__)

ex_service = ExtractorService()
es_service = ElasticService()
wp_service = WikiService()


@api.route("/analyze", methods=['POST'])
def analyze_ep():
    words = int(request.args.get('words', 2))
    top = int(request.args.get('top', 3))
    text = json.loads(request.data).get('text', None)

    key_phrases = None
    wp_articles = None
    if text:
        key_phrases = ex_service.extract(text, words, top)
        es_service.save(text, key_phrases)
        wp_articles = wp_service.search(key_phrases)
    else:
        abort(400, message='Body doesn\'t have "text" field!')

    return json.jsonify(key_phrases=key_phrases, wikipedia=wp_articles)


@api.route("/top", methods=['GET'])
def top_ep():
    count = request.args.get('count', 5)
    ...  # TODO
    return json.jsonify(count=count)


@api.route("/all", methods=['GET'])
def all_ep():
    ...  # TODO
    return json.jsonify(['text' + str(i) for i in range(5)])
