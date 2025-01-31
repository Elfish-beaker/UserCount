from fastapi import FastAPI, Request
from datetime import datetime
import uvicorn

app = FastAPI()

# Store active users
active_users = {}

@app.post("/track")
async def track_user(request: Request):
    data = await request.json()
    user_id = data.get("user_id")

    if not user_id:
        return {"error": "Invalid request"}

    active_users[user_id] = {
        "last_active": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        "ip": request.client.host
    }

    return {"message": "User activity recorded", "active_users": len(active_users)}

@app.get("/active_users")
async def get_active_users():
    return active_users

# For local testing
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
