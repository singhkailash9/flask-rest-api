from flask import jsonify, request, send_from_directory
from models import load_data, save_cards
from config import Config

def configure_routes(app):

    @app.route('/', methods=['GET'])
    def default():
        return jsonify({"message": "Welcome and start making API requests."})


    @app.route('/hello', methods=['GET'])
    def hello_world():
        hello = load_data(Config.HELLO_FILE)
        limit_hello_query = request.args.get('limit', '10')
        try:
            limit = int(limit_hello_query)
        except ValueError:
            limit = 10
        limit = max(1, min(limit, len(hello)))

        limited_data = hello[:limit]
        return jsonify(limited_data)

    @app.route('/python', methods=['GET'])
    def python_icon():
        return send_from_directory(app.static_folder, 'python.png', mimetype='image/png')

    @app.route('/cards', methods=['GET'])
    def get_cards():
        cards = load_data(Config.DATA_FILE)['cards']
        return jsonify(cards)

    @app.route('/cards/<name>', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def card_operations(name):
        data = load_data(Config.DATA_FILE)
        cards = data['cards']

        if request.method == 'GET':
            if name in cards:
                return jsonify({"card": name})
            else:
                return jsonify({"error": "Card not found"}), 404

        if request.method == 'POST':
            if name in cards:
                return jsonify({"error": "Card already exists"}), 400
            cards.append(name)
            save_cards(data)
            return jsonify({"message": f"Card {name} added successfully"})

        if request.method == 'PUT':
            new_name = request.json.get('new_name')
            if not new_name:
                return jsonify({"error": "No new card name provided"}), 400
            if name not in cards:
                return jsonify({"error": "Card not found"}), 404
            index = cards.index(name)
            cards[index] = new_name
            save_cards(data)
            return jsonify({"message": f"Card {name} updated to {new_name}"})

        if request.method == 'DELETE':
            if name not in cards:
                return jsonify({"error": "Card not found"}), 404
            cards.remove(name)
            save_cards(data)
            return jsonify({"message": f"Card {name} deleted successfully"})