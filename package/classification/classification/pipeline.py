from sklearn.pipeline import Pipeline
import preprocessor as pp 
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier as knn


DISCRETE_VARS =['age',
                'height(cm)',
                'eyesight(right)',
                'hearing(left)',
                'hearing(right)',
                'Urine protein',
                'dental caries']

CONTINOUS_VARS = [  'weight(kg)',
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


smoke_status = Pipeline(
    [
        ('LogTransformation', pp.LogTransformation(variable = CONTINOUS_VARS)), 
        ('NumericalImputer', pp.NumericImputer(variable= [CONTINOUS_VARS, DISCRETE_VARS])), 
        ('MinMaxScaler', MinMaxScaler()), 
        ('K-NearestNeighbor', knn(n_neighbors= 4))
    ]
)