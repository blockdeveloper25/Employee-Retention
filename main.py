from flask import Flask, render_template, request
from flask import Response, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/training', methods=['POST'])
@cross_origin()
def training_route_client():
    try:
        return Response("Training started", status=200)
    except ValueError:
        return Response("Error Occured! %s" % str(ValueError), status=500)
    except KeyError:
        return Response("Error Occurred! %s" % KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" % e)

if __name__ == '__main__':
    app.run()