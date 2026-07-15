```python
from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(title="AI Employee Agent - Storybook")
app.include_router(router)

@app.on_event("startup")
async def startup():
    print("🚀 AI Employee Agent System Started")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
