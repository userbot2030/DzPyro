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

ADMINS = [5779185981]

BL_GCAST = [-1002127258037, -1001537494273, -1002145494730]


BL_GCAST = [-1002127258037, -1001537494273, -1002145494730]


DEVS = [5779185981]

def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Ubot"])
