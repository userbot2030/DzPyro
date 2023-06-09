from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden

FSUB = "accdzuserbot"



async def joined(filter, client, update):
    if not FSUB:  
     return True
    user_id = update.from_user.id
    if user_id in GUA
     return True
    try:
        member = await client.get_chat_member(chat_id = FSUB, user_id = user_id)
    except UserNotParticipant:
        return False
    if not member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]:
        return False
    else:
        return True

accdz = filter.create(joined)
