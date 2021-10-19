from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
import os
import shutil
from tqdm import tqdm

@Client.on_message(filters.private & filters.video)
async def main(bot, m):
    if not os.path.isdir('temp/'):
        os.makedirs('temp/')
    await m.download('temp/v.mp4')
    os.system("ffmpeg -i temp/v.mp4 -r 10 -f image2 output_%05d.jpg")
    for file in tqdm(sort_alphanumeric(os.listdir("temp"))):
        await m.reply_photo(photo=f"temp/{file}")
