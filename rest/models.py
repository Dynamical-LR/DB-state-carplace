import pickle
import pydantic
import logging 
import pandas

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/models.log")
logger.addHandler(file_handler)

class ParkingPlaceRentDataModel(pydantic.BaseModel):
    """
    Implementation of the data form for prediction,
    contains validation methods with
    """
    def to_frame(self):
        features = []
        df = pandas.DataFrame()
        for feature, value in self.__dict__.items():
            if feature in features:
                df[feature] = value 
        return df

class ParkingPlaceRentModel(object):
    """
    Implementation of the model for 
    predicting which decision customer will make
    """
    def __init__(self, model_file: str):
        self.validate_model_extension(model_file)
        self._model = pickle.load(model_file)

    def _validate_model_extension(self, file_path: str):
        """
        Function validates extension of the model file
        Args:
            file_path - path to the model
        """
        ext = file_path.split(".")[-1]
        return ext == '.pkl'

    def predict_outcome(self, data: ParkingPlaceRentDataModel):
        df = data.to_frame()
        prediction = self.model.predict(df)
        return prediction

# creating new model
try:
    model_file = "models/"
    model = ParkingPlaceRentModel(model_file=model_file)
except Exception as err:
    logger.critical(err)
    raise SystemExit("Failed to initialize model")