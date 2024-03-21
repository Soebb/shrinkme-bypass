from bs4 import BeautifulSoup
import cloudscraper
import os, time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = os.environ.get('TOKEN')

def shrinkme(update, context):
    url = update.message['text']
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
    try: return update.message.reply_text(r.json()['url'])
    except: return update.message.reply_text("Something went wrong")


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text("Hi, I am shrinkme url bypass bot")


if __name__=='__main__':
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text, shrinkme))
    dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
