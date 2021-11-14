from flask import Blueprint, jsonify, session, request
from app.models import User, db
from app.forms import LoginForm
from app.forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required

dashboard_routes = Blueprint('dashboard', __name__)



@dashboard_routes.route('', methods=['GET'])
@login_required
def dashboard():
    return jsonify({"message": "Welcome to the dashboard!"})
