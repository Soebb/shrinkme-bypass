from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
import os

@Client.on_message(filters.private & filters.video)
async def main(bot, m):
    await m.download('plugins/v.mp4')
    os.system("ffmpeg -ss 15 -i plugins/v.mp4 -vframes 1 -q:v 2 plugins/output.jpg")
    await m.reply_photo(photo='plugins/output.jpg')
