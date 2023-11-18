import numpy as np 
import pandas as pd 

from classification.processing.data_management import load_pipeline
from classification.config import config
from classification.processing.validation import validate_input
from classification import __version__ as version
import logging

_logger = logging.getLogger(__name__)
pipeline_file_name = f'{config.PIPELINE_SAVE_FILE}{version}.pkl'
smoke_pipe = load_pipeline(file_name=pipeline_file_name)

def make_prediction(*, filename:str) -> dict: 
    data = pd.read_json(filename)
    df = validate_input(input_data= data)
    predictions = smoke_pipe.predict(df[config.FEATURES])
    output = np.exp(predictions)
    response = {'prediction': output, "version":version}
    _logger.info(
        f'Making predictionwoth model version: {version}'
        f'Inputs: {validate_input}'
        f'Predictions: {response}'
    )
    return response
