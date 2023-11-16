import pandas as pd
import numpy as np 
from pipeline import smoke_status
from classification.processing.data_management import load_data, load_pipeline, save_pipeline
from classification.config import config
from sklearn.model_selection import train_test_split
import joblib

def run_training() -> None: 
    data = load_data(file_name='train.csv')
    x_train, x_test, y_train, y_test = train_test_split(
        data[config.FEATURES], data[config.TARGET], test_size=0.1, random_state= 0
    )
    smoke_status.fit(x_train, y_train)
    print('Training........')
    save_pipeline(pipeline_to_persist=smoke_status)

if __name__=="__main__":
    run_training()