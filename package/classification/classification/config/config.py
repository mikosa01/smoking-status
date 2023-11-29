import pathlib 
# import classification
import os 



# PACKAGE_ROOT = pathlib.Path(classification.__file__).resolve().parent
PACKAGE_ROOT = pathlib.Path(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
DATASET_DIR = PACKAGE_ROOT / 'dataset'
TRAINED_MODEL_DIR = PACKAGE_ROOT/'trained_model'

TESTING_DATA_FILE = DATASET_DIR/'test.csv'
TRAINING_DATA_FILE = DATASET_DIR/'train.csv'
TARGET = 'smoking'

FEATURES = ['age',
            'height(cm)',
            'weight(kg)',
            'waist(cm)',
            'eyesight(left)',
            'eyesight(right)',
            'hearing(left)',
            'hearing(right)',
            'systolic',
            'relaxation',
            'fasting blood sugar',
            'Cholesterol',
            'triglyceride',
            'HDL',
            'LDL',
            'hemoglobin',
            'Urine protein',
            'serum creatinine',
            'AST',
            'ALT',
            'Gtp',
            'dental caries']

DISCRETE_VARS =['age',
                'height(cm)',
                'eyesight(right)',
                'hearing(left)',
                'hearing(right)',
                'Urine protein',
                'dental caries']

CONTINOUS_VARS = ['weight(kg)',
                  'waist(cm)',
                  'eyesight(left)',
                  'systolic',
                  'relaxation',
                  'fasting blood sugar',
                  'Cholesterol',
                  'triglyceride',
                  'HDL',
                  'LDL',
                  'hemoglobin',
                  'serum creatinine',
                  'AST',
                  'ALT',
                  'Gtp']

MODEL_NAME = 'K-NEAREST_NEIGHBOR_CLASSIFIER'
PIPELINE_SAVE_FILE = f"{MODEL_NAME}_output_v"
