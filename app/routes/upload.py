from fastapi import APIRouter, File, UploadFile, Request
from fastapi.responses import JSONResponse
import shutil
import os
from uuid import uuid4

router = APIRouter()

UPLOAD_DIR = "uploaded_images"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/image")
async def upload_image(request: Request, file: UploadFile = File(...)):
    filename = f"{uuid4().hex}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Dynamic URL for both local and Render
    base_url = str(request.base_url).rstrip("/")
    image_url = f"{base_url}/uploaded_images/{filename}"
    return JSONResponse({"image_url": image_url})
