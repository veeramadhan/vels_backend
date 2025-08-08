from pydantic import BaseModel

class Property(BaseModel):
    title: str
    location: str
    price: float
    image_url: str
    description: str
