import numpy as np 
import pandas as pd 

from classification.processing.data_management import load_pipeline
from classification.config import config

pipeline_file_name = 'classification.pkl'
smoke_pipe = load_pipeline(file_name=pipeline_file_name)

def make_prediction(*, filename:str) -> dict: 
    data = pd.read_json(filename)
    predictions = smoke_pipe.predict(data[config.FEATURES])
    output = np.exp(predictions)
    response = {'prediction': output}
    return response
