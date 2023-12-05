import pandas as pd 
import numpy as np 
import joblib
import typing as t
from sklearn.pipeline import Pipeline
from classification.config import config
from classification.pipeline import smoke_status
import logging 
from classification import __version__ as _version

_logger = logging.getLogger(__name__)

def load_data(*, file_name:str) ->pd.DataFrame: 
    data = pd.read_csv(f'{config.DATASET_DIR}/{file_name}')
    return data 

def save_pipeline(*, pipeline_to_persist) ->None:
    save_file_name = f'{config.PIPELINE_SAVE_FILE}{_version}.pkl'
    save_path = config.TRAINED_MODEL_DIR / save_file_name
    remove_old_pipelines(files_to_keep=[save_file_name])
    joblib.dump(pipeline_to_persist, save_path)
    _logger.info(f'saved pipeline : {save_file_name}')

def load_pipeline(*, file_name:str) -> Pipeline: 
    file_path = config.TRAINED_MODEL_DIR/file_name
    saved_pipeline = joblib.load(filename=file_path)
    return saved_pipeline

def remove_old_pipelines(*, files_to_keep: t.List[str]) -> None: 
    do_not_delete = files_to_keep + ['__init__.py']
    for model_file in config.TRAINED_MODEL_DIR.iterdir(): 
        if model_file.name not in do_not_delete: 
            model_file.unlink()
