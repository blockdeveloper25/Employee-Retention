from wsgiref import simple_server
from flask import Flask, request, render_template
from flask import Response
import flask_monitoringdashboard as dashboard
import pandas as pd
import os
from flask_cors import CORS, cross_origin
from apps.training.train_model import TrainModel
from apps.prediction.predict_model import PredictModel
from apps.core.config import Config
"""
*****************************************************************************
*
* filename:       main.py
* version:        1.0
* author:         CODESTUDIO
* creation date:  28-APRIL-2025
*
* change history:
*
* who             when           version  change (include bug# if apply)
* ----------      -----------    -------  ------------------------------
* Sujair          28-APRIL-2025    1.0      initial creation
*
*
* description:    flask main file to run application
*
****************************************************************************
"""

app = Flask(__name__)


@app.route('/training', methods=['POST']) 
@cross_origin()
def training_route_client():
    """
    * method: training_route_client
    * description: method to call training route
    * return: none
    *
    * who             when           version  change (include bug# if apply)
    * ----------      -----------    -------  ------------------------------
    * Sujair          28-APRIL-2025    1.0      initial creation
    *
    * Parameters
    *   None
    """
    try:
        config = Config()
        #get run id
        run_id = config.get_run_id()
        data_path = config.training_data_path
        #trainmodel object initialization
        trainModel=TrainModel(run_id,data_path)
        #training the model
        trainModel.training_model()
        return Response("Training successfull! and its RunID is : "+str(run_id))
    except ValueError:
        return Response("Error Occurred! %s" % ValueError, status=400)
    except KeyError:
        return Response("Error Occurred! %s" % KeyError, status=401)
    except Exception as e:
        return Response("Error Occurred! %s" % e)

if __name__ == '__main__':
    app.run(port=5001, debug=True)