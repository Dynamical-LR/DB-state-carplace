import fastapi
from fastapi import responses 
from rest import models
import logging 

logger = logging.getLogger(__name__)
handler = logging.FileHandler(filename="logs/rest.log")
logger.addHandler(handler)

def healthcheck():
    """
    Function used for monitoring health of the
    web application
    """
    return responses.Response(
        status_code=200
    )

async def predict_parking_place_rent(application_data: models.ParkingPlaceRentDataModel):
    """
    Function predicts parking place rent decision 
    of the customer
    """
    try:
        prediction_status = models.model.predict_outcome(
            data=application_data
        )
        return fastapi.responses.JSONResponse(
            status_code=201,
            content={
                "predicted_status": prediction_status
            }
        )
    except Exception as err:
        logger.error(err)
        return fastapi.exceptions.HTTPException(
            status_code=501,
            detail='Server Prediction Model Error'
        )