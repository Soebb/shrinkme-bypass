from bs4 import BeautifulSoup
import cloudscraper
import os, time
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


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
I am test Bot.
"""

START_BTN = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("Source Code", url="https://github.com/samadii/"),
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


@Bot.on_message(filters.private & filters.text)
async def main(_, m):
    result = shrinkme(m.text)
    await m.reply(result)

def shrinkme(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    DOMAIN = "https://en.shrinke.me/"
    url = url[:-1] if url[-1] == '/' else url
    code = url.split("/")[-1]
    final_url = f"{DOMAIN}/{code}"
    ref = "https://mrproblogger.com/"
    h = {"referer": ref}
    resp = client.get(final_url,headers=h)
    soup = BeautifulSoup(resp.content, "html.parser")
    inputs = soup.find_all("input")
    data = { input.get('name'): input.get('value') for input in inputs }
    #print(data)
    h = { "x-requested-with": "XMLHttpRequest" }
    time.sleep(15)
    r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
    try: return r.json()['url']
    except: return "Something went wrong :("


Bot.run()
