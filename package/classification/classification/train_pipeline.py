import pathlib

PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent
DATASET_DIR = PACKAGE_ROOT/'dataset'
TRAINED_MODEL_DIR = PACKAGE_ROOT/'datasets'

TESTING_DATA_FILE = DATASET_DIR/'test.csv'
TRAINING_DATA_FILE = DATASET_DIR/'train.csv'
TARGET = 'smoking'

FEATURES = ['age', 'height(cm)', 'eyesight(right)', 'hearing(left)', 'hearing(right)',
            'Urine protein', 'dental caries', 'weight(kg)', 'waist(cm)', 'eyesight(left)',
            'systolic', 'relaxation', 'fasting blood sugar', 'Cholesterol', 'triglyceride',
            'HDL', 'LDL', 'hemoglobin', 'serum creatinine', 'AST', 'ALT', 'Gtp']