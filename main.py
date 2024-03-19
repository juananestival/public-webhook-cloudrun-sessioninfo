import flask
from flask import request, Flask, jsonify
import logging
from flask_cors import CORS
import os
import json


app = Flask(__name__)
CORS(app)
app = Flask(__name__)

@app.post("/samplewh")
def sample_wh():
  output = {
    'sessionInfo': {
      'parameters': {
        'userAuthenticated': 'y',
        }
      }
  }
  response_json = json.dumps(output)
  return response_json
  # return flask.jsonify({"results": "output"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
