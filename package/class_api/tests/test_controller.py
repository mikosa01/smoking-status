import json 
import math

from classification.config import config as model_config
from classification.processing.data_management import load_data
from classification import __version__ as _version
from api import __version__ as api_version


def test_health_endpoint_returns_200(flask_test_client):
    reponse = flask_test_client.get('/smoke')
    assert reponse.status_code == 200


def test_version_endpoint_rturns_version(flask_test_client): 
    response = flask_test_client.get('/version')

    assert response.status_code == 200
    response_json = json.loads(response.data)

    assert response_json['model_version'] == _version
    assert response_json['api_version'] == api_version


def test_prediction_endpoint_returns_prediction(flask_test_client): 
    test_data = load_data(file_name= 'test.csv')
    post_json = test_data[0:1].to_json(orient='records')

    response = flask_test_client.post('/v1/predict/classification', json=json.loads(post_json))

    assert response.status_code == 200 
    response_json = json.loads(response.data)
    prediction = response_json.get('predictions')
    response_version = response_json['version']
    # print(response_json)
    # assert math.ceil(predictions) == 1.0
    assert prediction is  not None
    assert math.ceil(prediction[0]) == 0
    assert response_version == _version