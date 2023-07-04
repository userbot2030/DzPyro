# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

import asyncio
from pyrogram import Client, filters, raw
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import Message
from . import *
from ubotlibs.ubot.helper.basic import edit_or_reply


@Ubot(["limit"], cmds)
async def spamban(client: Client, m: Message):
    await client.unblock_user("SpamBot")
    bot_info = await client.resolve_peer("SpamBot")
    response = await client.send(
        raw.functions.messages.StartBot(
            bot=bot_info,
            peer=bot_info,
            random_id=client.rnd_id(),
            start_param="start",
        )
    )
    mm = await m.reply_text("`Processing...`")
    await asyncio.sleep(1)
    await mm.delete()
    status = await client.get_messages("SpamBot", response.updates[1].message.id + 1)
    await m.edit_text(f"{status.text}")
    return await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))

add_command_help(
    "limit",
    [
        [f"limit", "Cek limit/batasan akun."],
    ],
)
