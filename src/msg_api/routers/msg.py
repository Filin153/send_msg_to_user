from fastapi import APIRouter

from send.rabbitmq import add_new_msg_task
from send.schemas import CreateMessage

router = APIRouter(
    prefix="/msg",
)


@router.post("/", response_model=CreateMessage)
async def create_message(create_message: CreateMessage):
    await add_new_msg_task(create_message)
    return True
