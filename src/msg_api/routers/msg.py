from fastapi import APIRouter
from schemas import CreateMessage
from rabbitmq import add_new_msg_task

router = APIRouter(
    prefix="/msg",
)

@router.post("/", response_model=CreateMessage)
async def create_message(create_message: CreateMessage):
    await add_new_msg_task(create_message)
    return create_message
