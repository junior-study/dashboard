from datetime import timedelta
from flask import Blueprint,Flask, jsonify, request, session, escape, make_response, send_file

mod = Blueprint('agit', __name__)

@mod.route('/notices', methods=['GET'])
def _agitNotices():

    return jsonify(True)