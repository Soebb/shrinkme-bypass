import os
from config import Config

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait

CAPTION=Config.CAPTION

@Client.on_message(filters.media & filters.channel)
async def caption(client, message: Message):
    media = message.audio or message.video or message.document or message.animation
    if (media is not None) and (media.file_name is not None):
        file = media.file_name
    await message.edit(CAPTION)
