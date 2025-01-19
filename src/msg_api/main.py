from fastapi import FastAPI
from send.rabbitmq import close_rabbitmq
from routers import router as api_router


app = FastAPI(
    title="Message API",

)

@app.on_event("shutdown")
async def shutdown_event():
    await close_rabbitmq()

app.include_router(api_router)
