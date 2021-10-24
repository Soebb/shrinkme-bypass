
import requests
import numpy as np
import os, datetime
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

if "BOT_TOKEN" in os.environ:
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = os.environ.get("API_ID")
    API_HASH = os.environ.get("API_HASH")
else:
    BOT_TOKEN = "2055078811:AAE-MoEGbgR1I22igfOtfQCGEf20VC2KRTs"
    API_ID = "4328913"
    API_HASH = "3230ec801f78a517c9a2ad6bebb7f7b4"

Bot = Client(
    "Bot",
    bot_token = BOT_TOKEN,
    api_id = API_ID,
    api_hash = API_HASH
)

START_TXT = """
Hi {}
I am subtitle extractor Bot.
> `I can extract hard-coded subtitle from videos.`
Send me a video to get started.
"""

START_BTN = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("Source Code", url="https://github.com/samadii/VidSubExtract-Bot"),
        ]]
    )


@Bot.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TXT.format(update.from_user.mention)
    reply_markup = START_BTN
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )


#language
LANG="fas"


@Bot.on_message(filters.private & filters.video)
async def main(bot, m):
    videopath = "temp/thevideo.mp4"
    await m.download(videopath)
    sub_count = 0
    s = 0
    e = m.video.duration
    step = 0.1
    intervals = [round(num, 2) for num in np.linspace(s,e,(e-s)*int(1/step)+1).tolist()]
    repeated_count = 0
    last_text = "last_text"
    duplicate = False
    for interval in intervals:
        try:
            os.system(f"ffmpeg -ss {interval} -i {videopath} -vframes 1 -q:v 2 -y temp/output.jpg")
            im = Image.open("temp/output.jpg")
            text = pytesseract.image_to_string(im, LANG)
        except:
            text = None
            pass

        if (text != None) and (text[:1].isspace() == False):
            if (len(text.rsplit()) < 3) and (len(last_text.rsplit()) < 3):
                if (len(text.rsplit()) == 2) and (len(last_text.rsplit()) == 2):
                    if (text.rsplit()[0] == last_text.rsplit()[0]) or (text.rsplit()[1] == text.rsplit()[0]):
                        duplicate = True
                        repeated_count += 1
                    else:
                        duplicate = False
                elif (len(text.rsplit()) == 1) and (len(last_text.rsplit()) == 1):
                    if text == last_text:
                        duplicate = True
                        repeated_count += 1
                    else:
                        duplicate = False
            elif (len(text.rsplit()) => 3) and (len(last_text.rsplit()) => 3):
                try:
                    if ((text.rsplit(' ')[0] == last_text.rsplit(' ')[0]) and (text.rsplit(' ')[1] == last_text.rsplit(' ')[1])) or ((text.rsplit(' ')[0] == last_text.rsplit(' ')[0]) and (text.rsplit(' ')[2] == last_text.rsplit(' ')[2])) or ((text.rsplit(' ')[2] == last_text.rsplit(' ')[2]) and (text.rsplit(' ')[1] == last_text.rsplit(' ')[1])):
                        duplicate = True
                        repeated_count += 1
                    else:
                        duplicate = False
                except IndexError:
                    duplicate = False
            else:
                duplicate = False

            if duplicate == False :
                if repeated_count != 0 :
                    # Write previous duplicates
                    sub_count += 1
                    from_time = str(datetime.datetime.fromtimestamp(interval-repeated_count*0.1)+datetime.timedelta(hours=0)).split(' ')[1][:12]
                    to_time = str(datetime.datetime.fromtimestamp(interval-0.1)+datetime.timedelta(hours=0)).split(' ')[1][:12]
                    f.write(str(sub_count) + "\n" + from_time + " --> " + to_time + "\n" + last_text + "\n\n")
                    # Write new
                    sub_count += 1
                    from_time = str(datetime.datetime.fromtimestamp(interval)+datetime.timedelta(hours=0)).split(' ')[1][:12]
                    to_time = str(datetime.datetime.fromtimestamp(interval+0.1)+datetime.timedelta(hours=0)).split(' ')[1][:12]
                    f.write(str(sub_count) + "\n" + from_time + " --> " + to_time + "\n" + text + "\n\n")
                    repeated_count = 0
                else:
                    # Write new
                    sub_count += 1
                    from_time = str(datetime.datetime.fromtimestamp(interval)+datetime.timedelta(hours=0)).split(' ')[1][:12]
                    to_time = str(datetime.datetime.fromtimestamp(interval+0.1)+datetime.timedelta(hours=0)).split(' ')[1][:12]
                    f = open("temp/srt.srt", "a+", encoding="utf-8")
                    f.write(str(sub_count) + "\n" + from_time + " --> " + to_time + "\n" + text + "\n\n")
                last_text = text
    f.close
    await m.reply_document(document="temp/srt.srt" ,caption=m.video.file_name)
    os.remove("temp/srt.srt")


Bot.run()
