from fastapi import FastAPI
from pydantic import BaseModel,Field,conint,confloat
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from typing import Literal
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
import requests
import pickle


app = FastAPI(title = "FLIGHT PRICE PREDICTIONS API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # ⚠️ Allow all origins for now; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open(os.path.join("static", "new_index.html"), "r", encoding="utf-8") as f:
        return f.read()


MODEL_PATH = "flight_model.pkl"
MODEL_URL = "https://huggingface.co/kishlayambastha/flight-price-model/resolve/main/flights_new.pkl"

# download model if not present
if not os.path.exists(MODEL_PATH):
    print("Downloading model from Hugging Face...")
    r = requests.get(MODEL_URL)
    open(MODEL_PATH, 'wb').write(r.content)
    print("Model downloaded!")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


# with open("flights_new.pkl","rb") as f:
#     model = pickle.load(f)


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open(os.path.join("static", "index.html"), "r", encoding="utf-8") as f:
        return f.read()


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