from fastapi import APIRouter

from send.mail import CreateMessage, Mail

router = APIRouter(
    prefix="/msg",
)
mail = Mail()


@router.post("/")
async def create_message(create_message: CreateMessage):
    await mail.send_msg(create_message)
    return True
