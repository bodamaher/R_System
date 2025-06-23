from pymongo import MongoClient
import pandas as pd

def get_workspace_data():
    client = MongoClient("mongodb+srv://mohamedalibadawypr:AQpmE96i6p7O7Zpj@worklocate.ljup3kj.mongodb.net/workLocate?retryWrites=true&w=majority")
    db = client["workLocate"]
    collection = db["workingspaces"]
    data = list(collection.find())
    df = pd.DataFrame(data)

    df["latitude"] = df["location"].apply(lambda x: x["coordinates"][0] if isinstance(x, dict) else None)
    df["longitude"] = df["location"].apply(lambda x: x["coordinates"][1] if isinstance(x, dict) else None)
    df["amenities_count"] = df["amenities"].apply(lambda x: len(x) if isinstance(x, list) else 0)

    return df[["name", "amenities", "averageRating", "latitude", "longitude", "amenities_count"]]
