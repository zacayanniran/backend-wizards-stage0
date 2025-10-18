from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import os
from dotenv import load_dotenv
import httpx
import logging
from typing import Dict, Any

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Backend Wizards Stage 0", version="1.0.0")

# CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# User configuration
USER_CONFIG = {
    "email": os.getenv("EMAIL", "zacchdipo@gmail.com"),
    "name": os.getenv("NAME", "Zacchaeus Ayanniran"),
    "stack": os.getenv("STACK", "Python/FastAPI")
}

@app.get("/me", response_model=Dict[str, Any])
async def get_profile():
    """
    GET /me - Returns user profile with dynamic cat fact
    """
    try:
        # Dynamic UTC timestamp (ISO 8601)
        timestamp = datetime.utcnow().isoformat() + "Z"
        
        # Fetch cat fact with timeout
        timeout = httpx.Timeout(5.0)
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.get("https://catfact.ninja/fact")
            response.raise_for_status()
            cat_data = response.json()
            fact = cat_data.get("fact", "Cats are amazing creatures!")
        
        logger.info(f"Successfully fetched cat fact: {fact[:50]}...")
        
        # Response structure (EXACT FORMAT REQUIRED)
        return {
            "status": "success",
            "user": USER_CONFIG,
            "timestamp": timestamp,
            "fact": fact
        }
        
    except httpx.RequestError as e:
        logger.error(f"Cat API error: {e}")
        # Graceful fallback
        return {
            "status": "success",
            "user": USER_CONFIG,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "fact": "When a cat purrs, it's not just happy - it's healing itself!"
        }
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/")
async def root():
    return {"message": "Backend Wizards Stage 0 API - Visit /me for profile!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
