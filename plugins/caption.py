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
        if ep in m.split()[3]:
            E = m.split()[3]
        if ep in m.split()[4]:
            E = m.split()[4]
        if ep in m.split()[5]:
            E = m.split()[5]
        if ep in m.split()[6]:
            E = m.split()[6]
        if ep in m.split()[7]:
            E = m.split()[7]
        if ep in m.split()[8]:
            E = m.split()[8]
        if ep in m.split()[9]:
            E = m.split()[9]
        e = E.replace("E", " ")
        if '720P' in m:
            Q = '720'
        if '480P' in m:
            Q = '480'
        if '1080P' in m:
            Q = '1080'
        if '240P' in m:
            Q = '240'
        N = m.replace("@dlmacvin2 -", " ")
        n = N.split(f"{E}")[0]
        await message.edit(
