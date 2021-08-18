import os
from config import Config

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait

@Client.on_message(filters.media & filters.channel)
async def caption(client, message: Message):
    media = message.audio or message.video or message.document or message.animation
    if (media is not None) and (media.file_name is not None):
        m = media.file_name
        epi = m.split(None
        ep = "E1" or "E2" or "E3" or "E4" or "E5" or "E6" or "E7" or "E8" or "E9"
        if '720P' in m:
            y = '720'
        if '480P' in m:
            y = '480'
        if '1080P' in m:
            y = '1080'
        if '240P' in m:
            y = '240'


    await message.edit(
