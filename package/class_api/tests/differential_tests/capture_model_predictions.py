import pandas as pd 
from classification.predict import make_prediction
from classification.processing.data_management import load_data

from api import config


def capture_predictions():

    save_file = 'test_data_prediction.csv'
    test_data = load_data(file_name='test.csv')
    multiple_test_input = test_data[90:600]

    predictions = make_prediction(filename=multiple_test_input)

    prediction_df = pd.DataFrame(predictions)

    prediction_df.to_csv(
        f'{config.PACKAGE_ROOT.parent}/{save_file}'      
                )
    

if __name__ == '__main__':
    capture_predictions()