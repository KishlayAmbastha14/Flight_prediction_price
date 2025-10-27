from fastapi import FastAPI
from pydantic import BaseModel,Field,conint,confloat
from fastapi.middleware.cors import CORSMiddleware
import pickle
import pandas as pd
from typing import Literal

app = FastAPI(title = "FLIGHT PRICE PREDICTIONS API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # ⚠️ Allow all origins for now; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# -

with open("flights_new.pkl","rb") as f:
    model = pickle.load(f)

@app.get("/")
async def flights():
    return {"message":"FLight is landing"}

class FlightsInput(BaseModel):
    airline: Literal["Air India", "Indigo", "SpiceJet", "Vistara", "GO_FIRST", "AirAsia"] = Field(...,description='name of airline company')

    source_city: Literal[ "Delhi", "Mumbai", "Bangalore", "Kolkata", "Hyderabad", "Chennai"]
    destination_city: str
    departure_time: str
    arrival_time: str
    class_: str
    duration: float
    days_left: int
    stops: str

@app.post("/predict")
async def predict_price(data:FlightsInput):
    input_df = pd.DataFrame([
        {
        "airline": data.airline,
        "source_city": data.source_city,
        "destination_city": data.destination_city,
        "departure_time": data.departure_time,
        "arrival_time": data.arrival_time,
        "class": data.class_,
        "duration": data.duration,
        "days_left": data.days_left,
        "stops": data.stops
        }
    ])

    predictions = model.predict(input_df)[0]
    return {"Predicted Price": int(predictions)}