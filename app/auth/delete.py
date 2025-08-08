from fastapi import APIRouter, HTTPException
from app.database import db
from bson import ObjectId

router = APIRouter()

@router.delete("/delete/{property_id}")
def delete_property(property_id: str):
    result = db.properties.delete_one({"_id": ObjectId(property_id)})

    if result.deleted_count == 1:
        return {"message": "Property deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Property not found")
