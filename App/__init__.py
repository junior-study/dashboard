# -*- coding: utf-8i -*-
from flask import Flask, jsonify, request, session, make_response, blueprints


app = Flask(__name__)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=60)
app.json_encoder = AlchemyEncoder
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)