from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.routes import property, upload
from app.auth import login, delete

app = FastAPI()

# CORS settings - adjust frontend URL if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://vels-promotors.vercel.app/", "https://vels-promotors-fwyd2f78b-veeramadhans-projects.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route registrations
app.include_router(property.router, prefix="/api/property")
app.include_router(login.router, prefix="/api/auth")
app.include_router(delete.router, prefix="/api/property")
app.include_router(upload.router, prefix="/api/upload")

# Serve static files (uploaded images)
app.mount("/uploaded_images", StaticFiles(directory="uploaded_images"), name="uploaded_images")

# Root endpoint (optional, avoids 404 at /)
@app.get("/")
def root():
    return {"message": "Backend is running"}
