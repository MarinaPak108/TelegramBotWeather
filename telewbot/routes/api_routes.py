from flask import Blueprint, jsonify
from telewbot.services.external import fetch_data_from_api

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/data/<string:endpoint>', methods=['GET'])
def get_data(endpoint):
    try:
        data = fetch_data_from_api(endpoint)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
