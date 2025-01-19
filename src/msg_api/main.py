from fastapi import FastAPI

from routers import router as api_router
from send.rabbitmq import close_rabbitmq

app = FastAPI(
    title="Message API",

)


@app.on_event("shutdown")
async def shutdown_event():
    await close_rabbitmq()


app.include_router(api_router)
