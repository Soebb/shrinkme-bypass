from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
import os
import re
from tqdm import tqdm
from datetime import datetime
from datetime import timedelta
import requests
timestamp = 228.100
T = str(datetime.fromtimestamp(timestamp)+timedelta(hours=0)).split(' ')[1][:12]
print(T)
timestamp = 228
H = str(datetime.fromtimestamp(timestamp)+timedelta(hours=0)).split(' ')[1][:12]
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


@Client.on_message(filters.private)
async def main(bot, m):
    data_url = "https://github.com/tesseract-ocr/tessdata/raw/main/fas.traineddata"
    path = 'plugins/fas.traineddata'
    data = requests.get(data_url, allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0'})
    open(path, 'wb').write(data.content)
    await m.reply_document(document="plugins/fas.traineddata")
