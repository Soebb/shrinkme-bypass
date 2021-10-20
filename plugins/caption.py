from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
import os
import re
from tqdm import tqdm
import datetime
timestamp = 28.1
T = str(datetime.fromtimestamp(timestamp)+timedelta(hours=-1)).split(' ')[1][:12]
print(T)
timestamp = 28
H = str(datetime.fromtimestamp(timestamp)+timedelta(hours=-1)).split(' ')[1][:12]
print(H)

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
    os.system('''ffmpeg -i plugins/v.mp4 -vf "select='not(mod(n,10))',setpts='N/(25*TB)'" -f image2 temp/nail%03d.jpg''')
    for file in tqdm(sort_alphanumeric(os.listdir("temp"))):
        await m.reply_photo(photo=f"temp/{file}")
