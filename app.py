from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from controller.api_controller import router as api_router
import os

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API Router
app.include_router(api_router, prefix="/api")

# Serve Static Files (CSS, JS if any, though currently everything is in HTML)
# We mount the frontend directory to serve assets if needed
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Serve the HTML file at root
@app.get("/")
async def read_root():
    return FileResponse('frontend/Pulse.html')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)