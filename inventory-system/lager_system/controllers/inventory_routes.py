from flask import Blueprint, render_template, request, jsonify
from lager_controller import LagerController

inventory_routes = Blueprint('inventory_routes', __name__)
lager = LagerController()

@inventory_routes.route('/')
def index():
    return render_template('index.html')

@inventory_routes.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    results = [str(item) for item in lager.search_item(query)]
    return jsonify(results)

@inventory_routes.route('/items', methods=['GET'])
def get_items():
    items = [str(item) for item in lager.get_all_items()]
    return jsonify(items)

@inventory_routes.route('/add', methods=['POST'])
def add_item():
    data = request.json
    lager.add_item(data['name'], data['quantity'], data['location'])
    return jsonify({'status': 'success'})

@inventory_routes.route('/update', methods=['POST'])
def update_item():
    data = request.json
    lager.update_item(data['name'], data['new_quantity'], data.get('new_off_site_location', 'N/A'))
    return jsonify({'status': 'success'})

@inventory_routes.route('/remove', methods=['POST'])
def remove_item():
    data = request.json
    lager.remove_item(data['name'])
    return jsonify({'status': 'success'})
