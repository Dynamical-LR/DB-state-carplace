import logging 
import fastapi
import os
from rest import controllers
from fastapi.middleware import cors

logger = logging.getLogger(__name__)

# Parsing environment variables
APPLICATION_VERSION = os.environ.get("APPLICATION_VERSION", "0.0.1")
ALLOWED_METHODS = os.environ.get("ALLOWED_METHODS", "*")
ALLOWED_HEADERS = os.environ.get("ALLOWED_HEADERS", "*")
ALLOWED_ORIGINS = os.environ.get("ALLOWED_ORIGINS", "*")

application = fastapi.FastAPI(
        version=APPLICATION_VERSION,
)
try:
    # initializing rest controllers for the model
    application.add_api_route(
        endpoint=controllers.healthcheck,
        path='/healthcheck/',
        methods=['GET'],
    )

    application.add_api_route(
        endpoint=controllers.predict_parking_place_rent,
        path='/predict/parking/place/rent/',
        methods=['POST']
    )

    # initializing middlewares
    application.add_middleware(
        middleware_class=cors.CORSMiddleware,
        allow_origins=ALLOWED_ORIGINS,
        allow_headers=ALLOWED_HEADERS,
        allow_methods=['POST', 'GET', 'OPTIONS']
    )

except Exception as err:
    logger.error(err)
    raise SystemExit("Failed to initialize REST Endpoints / Middlewares, check logs")