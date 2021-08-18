import os
from config import Config

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait

@Client.on_message(filters.media & filters.channel)
async def caption(client, message: Message):
    media = message.video or message.document
    if (media is not None) and (media.file_name is not None):
        m = media.file_name
        ep = "E0" or "E1" or "E2" or "E3" or "E4" or "E5" or "E6" or "E7" or "E8" or "E9"
        if '720P' in m:
            Q = '720'
        if '480P' in m:
            Q = '480'
        if '1080P' in m:
            Q = '1080'
        if '240P' in m:
            Q = '240'
        N = m.replace("@dlmacvin2 -", " ")
        if ep in N.split()[1]:
            E = N.split()[1]
        if ep in N.split()[2]:
            E = N.split()[2]
        if ep in N.split()[3]:
            E = N.split()[3]
        if ep in N.split()[4]:
            E = N.split()[4]
        if ep in N.split()[5]:
            E = N.split()[5]
        if ep in N.split()[6]:
            E = N.split()[6]
        if ep in N.split()[7]:
            E = N.split()[7]
        if ep in N.split()[8]:
            E = N.split()[8]
        if ep in N.split()[9]:
            E = N.split()[9]
        e = E.replace("E", " ")
        n = N.split(f"{E}")[0]
        await message.edit(
