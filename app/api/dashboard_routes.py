from flask import Blueprint, jsonify
from flask_login import login_required

dashboard_routes = Blueprint('dashboard', __name__)



@dashboard_routes.route('', methods=['GET'])
@login_required
def dashboard():
    return jsonify({"message": "Welcome to the dashboard!"})
