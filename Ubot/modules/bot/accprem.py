from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden

FSUB = "accdzuserbot"



async def fsub(filter, client, update):
    if not FSUB:  
     return True
    user_id = update.from_user.id
    if user_id in DEV
     return True
    if user_id in GUA
     return True
    if user_id in BLACK
     return True
    if user_id in ADMINS
     return True
    try:
        try:
            await bot.get_chat_member(FSUB, msg.from_user.id)
        except UserNotParticipant:
            if FSUB.isalpha():
                link = "https://t.me/" + FSUB
            try:
                await msg.reply(
                    f"TEXT",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("ADMIN", url="https://t.me/MSDZULQRNN")],
                        [InlineKeyboardButton("SUPPORT", url="https://t.me/MSPR0JECT"),
                         InlineKeyboardButton("SUPPORT", url="https://t.me/dzlog")],
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Kamu bukan admin!")

accdz = filter.create(fsub)
