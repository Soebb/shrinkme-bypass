from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait


@Client.on_message(filters.private & filters.video)
async def main(bot, m):
    await m.download('v.mp4')
    os.system("ffmpeg -ss 15 -i v.mp4 -vframes 1 -q:v 2 output.jpg")
    m.reply_do
