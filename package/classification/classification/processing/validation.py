import pandas as pd 
from package.classification.classification.config import config


def validate_input(*, input_data: pd.DataFrame) -> pd.DataFrame: 

    validate_data = input_data.copy()
    print("Columns in input_data:", input_data.columns)


    if (input_data[config.CONTINOUS_VARS] <= 0 ).any().any():
        vars_with_na_values = config.CONTINOUS_VARS[
            (input_data[config.CONTINOUS_VARS]<= 0).any()
        ]
        validate_data = validate_data[validate_data[vars_with_na_values]> 0]
    
    return validate_data