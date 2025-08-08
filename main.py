from fastapi import FastAPI
from app.routes import property, upload
from app.auth import login, delete
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# ✅ CORS settings - adjust frontend URL if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React/Next frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Route Registrations
app.include_router(property.router, prefix="/api/property")
app.include_router(login.router, prefix="/api/auth")
app.include_router(delete.router, prefix="/api/property")  # If delete is a separate file, this is fine
app.include_router(upload.router, prefix="/api/upload")    # For file upload

# ✅ Serve static files (uploaded images) from folder
app.mount("/uploaded_images", StaticFiles(directory="uploaded_images"), name="uploaded_images")
