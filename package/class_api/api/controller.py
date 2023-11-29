from flask import Blueprint, request, jsonify
from classification.predict import make_prediction
from classification import __version__ as _version
from api import __version__ as api_version 
from api.config import get_logger
from api.validation import validate_inputs

_logger = get_logger(logger_name= __name__)

prediction_app = Blueprint('prediction_app', __name__)

@prediction_app.route('/smoke', methods=['GET'])
def health():
    if request.method == 'GET': 
        _logger.info('health status OK')
        return 'ok'
    
@prediction_app.route('/version', methods=['GET'])
def version(): 
    if request.method == 'GET': 
        return jsonify({'model_version': _version, 
                        'api_version': api_version})
    
@prediction_app.route('/v1/predict/classification', methods = ['POST'])
def predict():
    if request.method == 'POST':
        json_data = request.get_json()
        _logger.debug(f'input: {json_data}')

        # result = make_prediction(filename= json_data)
        # _logger.info(f'Outputs: {result}')
        # data = validate_inputs(input_data= json_data)
        result = make_prediction(filename= json_data)
        _logger.debug(f'inputs: {result}')


        predictions = result.get('prediction')
        version = result.get('version')

        return jsonify({"predictions": predictions.tolist(), 
                        'version':version}) 
                        # "errors":errors})   