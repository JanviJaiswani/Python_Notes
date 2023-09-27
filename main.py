# import packages
from fastapi import FastAPI
import uvicorn
from database.db import get_db
from routes.solarplant_routes import solarplant_router
from routes.windturbine_routes import windturbine_router
from routes.experiment_routes import experiment_router
from routes.forecastsetup_routes import forecastsetup_router

app = FastAPI()

#Routers for the Experiment Site Setup
app.include_router(windturbine_router, prefix="/api", tags=["WindTurbines"])
app.include_router(solarplant_router, prefix="/api", tags=["SolarPlants"])

#Routers for the Experiment Site Setup
app.include_router(experiment_router, prefix="/api", tags=["experiments"])

#Routers for the Forecastsetup
app.include_router(forecastsetup_router, prefix="/api", tags=["Forecastsetup"])

if __name__ == "__main__":
    uvicorn.run(app)


