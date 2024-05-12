
import random
import time
import traceback
from sys import version as pyver
from datetime import datetime
import os
import shlex
import textwrap
import asyncio 
from gc import get_objects

from pyrogram import __version__ as pyrover
from pyrogram.enums import ParseMode
from pyrogram import *
from pyrogram.types import *
from Ubot.core.data import Data
from Ubot.core import *
from Ubot.core.db.accesdb import *
from pyrogram.raw.functions import Ping
from Ubot import CMD_HELP, StartTime, app, ids, cmds
from config import OWNER_ID

BOT_VER = "5.0.0"

WHITE = [5779185981, 5779185981, 5779185981, 5779185981, 5779185981, 5779185981, 5779185981]

BLACK = [5779185981]


def support():
    buttons = [
        [
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/Disney_storeDan"),
        ],
    ]
    return buttons

async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time
    

async def alive_function(message, answers):
    status = ""
    if message._client.me.id in BLACK:
        status = "[owner👤]"
    elif message._client.me.id == OWNER_ID:
        status = "[admin👥]"
    else:
        status = "[user🔥]"
    start = datetime.now()
    buttons = support()
    ex = await message._client.get_me()
    user = len(ids)
    remaining_days = await get_expired_date(ex.id)
    await message._client.invoke(Ping(ping_id=0))
    ping = (datetime.now() - start).microseconds / 1000
    uptime = await get_readable_time((time.time() - StartTime))
    msg = (
        f"𝘿𝘼𝙉-𝙐𝙎𝙀𝙍𝘽𝙊𝙏💎\n\n"
        f"<b> status: {status}</b>\n"
        f"<b> type: premium💎</b>\n"
        f"<b> expired:</b> <code>{remaining_days}</code>\n"
        f"<b> ping:</b> <code>{ping} ms</code>\n"
        f"<b> member:</b> <code>{user}</code>\n"
        f"<b> uptime:</b> <code>{uptime}</code>\n")
    answers.append(
        InlineQueryResultArticle(
            title="alive",
            input_message_content=InputTextMessageContent(
                msg, parse_mode=ParseMode.HTML, disable_web_page_preview=True
            ),
            reply_markup=InlineKeyboardMarkup(buttons)))
    return answers



async def help_function(answers):
    bttn = paginate_help(0, CMD_HELP, "helpme")
    answers.append(
        InlineQueryResultArticle(
            title="Help Article!",
            input_message_content=InputTextMessageContent(
                Data.text_help_menu.format(len(CMD_HELP))
            ),
            reply_markup=InlineKeyboardMarkup(bttn),
        )
    )
    return answers


@app.on_inline_query()
# @inline_wrapper
async def inline_query_handler(client: Client, query):
    try:
        text = query.query.strip().lower()
        string_given = query.query.lower()
        answers = []
        answerss = []
        if text.strip() == "":
            return
        elif text.split()[0] == "alive":
            m = [obj for obj in get_objects() if id(obj) == int(query.query.split(None, 1)[1])][0]
            answerss = await alive_function(m, answers)
            await client.answer_inline_query(query.id, results=answerss, cache_time=300)
        elif string_given.startswith("helper"):
            answers = await help_function(answers)
            await client.answer_inline_query(query.id, results=answers, cache_time=0)

    except Exception as e:
        e = traceback.format_exc()
        print(e, "InLine")
      
