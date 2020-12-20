from flask import Flask, jsonify, abort, make_response, request
from models import discs
from forms import DiscForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "wise_panda"


@app.route("/api/v1/discs/", methods=["GET"])
def discss_list_api_v1():
    return jsonify(discs.all())


@app.route("/api/v1/discs/", methods=["POST"])
def create_disc():
    if not request.json or not 'title' in request.json:
        abort(400)
    disc = {
        'id': discs.all()[-1]['id'] + 1,
        'author': request.json['author'],
        'title': request.json['title'],
        'genre': request.json['genre'],
        'year': request.json['year'],
        'description': request.json.get('description', ""),
        'recommend': False
    }
    discs.create(disc)
    return jsonify({'disc': disc}), 201


@app.route("/api/v1/disc/<int:disc_id>", methods=["GET"])
def get_disc(disc_id):
    disc = discs.get(disc_id)
    if not disc:
        abort(404)
    return jsonify({"disc": disc})


@app.route("/api/v1/discs/<int:disc_id>", methods=["PUT"])
def update_disc(disc_id):
    disc = discs.get(disc_id)
    if not disc:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'id' in data and not isinstance(data.get('id'), int),
        'author' in data and not isinstance(data.get('author'), str),
        'title' in data and not isinstance(data.get('title'), str),
        'genre' in data and not isinstance(data.get('genre'), str),
        'year' in data and not isinstance(data.get('year'), int),
        'description' in data and not isinstance(data.get('description'), str),
        'recommend' in data and not isinstance(data.get('recommend'), bool)
    ]):
        abort(400)
    disc = {
        'id': data.get('id', disc[-1]['id'] + 1),
        'author': data.get('author', disc['author']),
        'title': data.get('title', disc['title']),
        'genre': data.get('genre', disc['genre']),
        'year': data.get('year', disc['year']),       
        'description': data.get('description', disc['description']),
        'recommend': data.get('done', disc['recommend'])
    }
 
    discs.update(disc_id, disc)
    return jsonify({'disc': disc})


@app.route("/api/v1/discs/<int:disc_id>", methods=['DELETE'])
def delete_disc(disc_id):
    result = discs.delete(disc_id)
    if not result:
        abort(404)
    return jsonify({'result': result})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)


if __name__ == "__main__":
    app.run(debug=False)