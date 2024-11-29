from fastapi import FastAPI
from typing import List

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Recommendation service is running"}

@app.post("/recommendations/user/{user_id}")
async def recommend_for_user(user_id: int, count: int = 5):
    """
    Generate recommendations for a user based on their past activity.
    """
    # Placeholder recommendation logic
    return {
        "user_id": user_id,
        "recommendations": [
            {"service_id": i, "score": 0.9 - (i * 0.1)} for i in range(1, count + 1)
        ],
    }

@app.post("/recommendations/provider/{provider_id}")
async def recommend_jobs_for_provider(provider_id: int, count: int = 5):
    """
    Generate job recommendations for a provider based on their skills.
    """
    # Placeholder recommendation logic
    return {
        "provider_id": provider_id,
        "recommended_jobs": [
            {"job_id": i, "relevance": 0.95 - (i * 0.1)} for i in range(1, count + 1)
        ],
    }