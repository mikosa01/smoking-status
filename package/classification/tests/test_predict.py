import math

from classification.predict import make_prediction
from classification.processing.data_management import load_data

def test_make_prediction(): 

    test_data = load_data(file_name= 'test.csv')
    single_test_json = test_data[0:1].to_json(orient='records')

    subject = make_prediction(filename= single_test_json)

    assert subject is not None
    assert isinstance(subject.get('prediction')[0], float)
    assert math.ceil(subject.get('prediction')[0]) == 1