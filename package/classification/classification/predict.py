import numpy as np 
import typing as t
import pandas as pd 

from classification.processing.data_management import load_pipeline
from classification.config import config
from classification.processing.validation import validate_input
from classification import __version__ as version
import logging

_logger = logging.getLogger(__name__)
pipeline_file_name = f'{config.PIPELINE_SAVE_FILE}{version}.pkl'
smoke_pipe = load_pipeline(file_name=pipeline_file_name)

def make_prediction(*, filename:t.Union[pd.DataFrame, dict]) -> dict: 
    data = pd.DataFrame(filename)
    validate_data= validate_input(input_data= data)
    predictions = smoke_pipe.predict(validate_data[config.FEATURES])
    # output = np.exp(predictions)
    response = {'prediction': predictions, "version":version}
    _logger.info(
        f'Making prediction with model version: {version}'
        f'Inputs: {validate_input}'
        f'Predictions: {response}'
    )
    return response
