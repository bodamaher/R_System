
from fastapi import FastAPI
from pydantic import BaseModel
from recommender import recommend_nearby

app = FastAPI()

class Location(BaseModel):
    latitude: float
    longitude: float

@app.post("/recommend")
def recommend(location: Location):
    results = recommend_nearby(location.latitude, location.longitude)
    return results.to_dict(orient="records")
