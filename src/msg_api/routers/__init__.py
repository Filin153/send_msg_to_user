from .msg import router as msg_router

from fastapi import APIRouter

router = APIRouter(
    prefix="/api"
)

router.include_router(msg_router)
