import json 
from classification.config import config
from classification.processing.data_management import load_data

def test_prediction_endpoint_validate(flask_test_client):

    test_data = load_data(file_name= 'test.csv')
    test_json = test_data.to_json(orient= 'records')

    print(test_json[0])

    response = flask_test_client.post('/v1/predict/classification', json= json.loads(test_json))

    assert response.status_code == 200
    response_json = json.loads(response.data)
    predictions = response_json.get('predictions')
    errors = response_json.get('errors')

    assert response.status_code == 200
    response_json = json.loads(response.data)


    