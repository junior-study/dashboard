# -*- coding: utf-8i -*-
from flask import Flask, jsonify, request, session, make_response, blueprints
from App.Util.json_encoder import AlchemyEncoder
from datetime import timedelta, datetime
from App.DB.database import db_session

app = Flask(__name__)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=60)
app.json_encoder = AlchemyEncoder
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

'''

login 시 필요한 부분

'''
# @app.before_request
# def _beforeRequest():
#
#     return make_response(jsonify(status=False), 401)

'''

DB가 있을경우  한 세션으로 유지해서 끊지 안기때문에 매번 세션마다 DB세션을 
끊어주어야한다.

'''
@app.teardown_appcontext
def _shutdownSession(exception=None):
    db_session.remove()
    if exception and db_session.is_active:
        db_session.rollback()

from App.Agit import mod as agit
app.register_blueprint(agit, url_path='/agit')
from App.Author import mod as author
app.register_blueprint(author, url_path='/author')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)