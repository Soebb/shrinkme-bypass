from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
import os
import re
from tqdm import tqdm


def sort_alphanumeric(data):
    """Sort function to sort os.listdir() alphanumerically
    Helps to process audio files sequentially after splitting 
    Args:
        data : file name
    """
    
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)] 
    
    return sorted(data, key = alphanum_key)


@Client.on_message(filters.private & filters.video)
async def main(bot, m):
    if not os.path.isdir('temp/'):
        os.makedirs('temp/')
    await m.download('plugins/v.mp4')
    os.system("ffmpeg -i plugins/v.mp4 -r 1 -f image2 temp/output_%05d.jpg")
    for file in tqdm(sort_alphanumeric(os.listdir("temp"))):
        await m.reply_photo(photo=f"temp/{file}")
