import math

import pytest
from classification.config import config as model_config
from classification.predict import make_prediction
from classification.processing.data_management import load_data
from api import config


@pytest.mark.differential
def test_model_prediction_differential(
    *, save_file: str='test_data_prediction.csv'):

    # Given
    previous_model_df = load_data(file_name='test_data_prediction.csv')
    previous_model_prediction = previous_model_df['prediction'].values 
    test_data = load_data(file_name='test.csv')
    multiple_test_json = test_data[90:600]

    #When
    response = make_prediction(filename=multiple_test_json)
    current_model_predictions = response.get('predictions')

    #Then 
    # assert len(previous_model_prediction) == len(current_model_predictions)

    for previous_value, current_value in zip(previous_model_prediction, current_model_predictions): 

        previous_value = previous_value.item()
        current_value = current_value.item()

        assert math.isclose(previous_value, 
                            current_value,
                            rel_tol =model_config.ACCEPTABLE_MODEL_DIFFERNCE)