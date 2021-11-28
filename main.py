from pyromod import listen
import requests
import yt_dlp
import os, time
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
'''
files_path = [os.path.abspath(x) for x in os.listdir("app")]
print(files_path)
'''
if "BOT_TOKEN" in os.environ:
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = os.environ.get("API_ID")
    API_HASH = os.environ.get("API_HASH")
else:
    BOT_TOKEN = " "
    API_ID = " "
    API_HASH = " "

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


@Bot.on_message(filters.private & filters.video)
async def main(bot, m):
    await m.download("temp/v1.mp4")
    merge = await bot.ask(m.chat.id,'ویدیویی که میخوای ادغام شه؟بفرس', filters=filters.video)
    await bot.download_media(message=merge.video, file_name="temp/v2.mp4")
    os.system("/app/mkvmerge.exe -o temp/v3.mp4 temp/v1.mp4 +temp/v2.mp4")
    time.sleep(10)
    await m.reply_video(video="temp/v3.mp4")


Bot.run()
