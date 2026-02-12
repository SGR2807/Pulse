from fastapi import APIRouter, HTTPException
from repository.data_service import DataService
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()
data_service = DataService()

# Pydantic models for request validation (optional but good practice)
# For now, we can use dict to match the flexibility of the previous Flask app
# or define a loose model. Let's use dict for simplicity as the schema is complex.

@router.get("/data")
async def get_data():
    try:
        data = data_service.get_data()
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/data")
async def save_data(data: dict):
    try:
        result = data_service.save_data(data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))