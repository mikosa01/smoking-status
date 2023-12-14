import math

from classification.predict import make_prediction
from classification.processing.data_management import load_data

def test_make_prediction(): 

    test_data = load_data(file_name= 'test.csv')
    single_test_json = test_data[0:10]

    subject = make_prediction(filename= single_test_json)

    assert subject is not None
    assert isinstance(subject.get('prediction')[0], int)
    assert len(set(subject.get('prediction'))) == 2

def test_make_multiple_predictions():
    
    test_data = load_data(file_name='test.csv')
    original_data_lenght = len(test_data)
    multiple_test_json = test_data

    subject = make_prediction(filename= multiple_test_json)

    

    assert subject is not None 
    assert len(subject.get('prediction'))==106171
    assert len(subject.get('prediction')) == original_data_lenght