from fastapi import APIRouter
from app.models import Property
from app.database import db
from bson import ObjectId

router = APIRouter()

@router.post("/add")
def add_property(property: Property):
    db.properties.insert_one(property.dict())
    return {"message": "Property added successfully"}

@router.get("/")
def get_properties():
    properties = list(db.properties.find())
    for p in properties:
        p["_id"] = str(p["_id"])  # ✅ Convert ObjectId to string for frontend use
    return properties