from pyrogram import Client, filters
from Ubot import cmds, app, BOTLOG_CHATID
from Ubot.core import *
from Ubot.logging import LOGGER
from ubotlibs.ubot import Ubot
import os
import sys
from os import environ, execle, path, remove
from .help import add_command_help
add_command_help = add_command_help

ADMINS = [1759398415, 1337085565]

BL_GCAST = [-1001473548283, -1001871397896]


BL_UBOT = [-1001812143750]
DEVS = [1337085565]

def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Ubot"])
