from pyrogram import filters, Client

from .ai import *
from .data import *
from .func import *
from .inline import *
from .lgs import *
from .what import *
from .filter import *
from .constants import *

async def ajg(client):
    try:
        await client.join_chat("DezetStore")
        await client.join_chat("DezetSupport")
        await client.join_chat("")
    except BaseException:
        pass
