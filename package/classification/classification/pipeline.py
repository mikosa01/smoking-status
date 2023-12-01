from sklearn.pipeline import Pipeline
from classification.processing import preprocessor as pp 
from package.classification.classification.config import config
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier as knn
import logging

_logger = logging.getLogger(__name__)

smoke_status = Pipeline(
    [
        ('LogTransformation', pp.LogTransformation(variable = config.CONTINOUS_VARS)), 
        ('NumericalImputer', pp.NumericImputer(variable= config.FEATURES)), 
        ('MinMaxScaler', MinMaxScaler()), 
        (config.MODEL_NAME, knn(n_neighbors= 2))
    ]
)