from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait

@Client.on_message(filters.media & filters.channel)
async def caption(client, message: Message):
    media = message.video or message.document
    if (media is not None) and (media.file_name is not None):
        m = media.file_name
        if '720P' in m:
            Q = '720'
        if '480P' in m:
            Q = '480'
        if '1080P' in m:
            Q = '1080'
        if '240P' in m:
            Q = '240'
        N = m.replace("@dlmacvin2 -", " ").replace("@dlmacvin -", " ")
        if 'E0' in N:
            O = N.split("E0")[1]
            T = O.split()[0]
            E = '0' + f"{T}"
        if 'E1' in N:
            O = N.split("E1")[1]
            T = O.split()[0]
            E = '1' + f"{T}"
        if 'E2' in N:
            O = N.split("E2")[1]
            T = O.split()[0]
            E = '2' + f"{T}"
        if 'E3' in N:
            O = N.split("E3")[1]
            T = O.split()[0]
            E = '3' + f"{T}"
        if 'E4' in N:
            O = N.split("E4")[1]
            T = O.split()[0]
            E = '4' + f"{T}"
        if 'E5' in N:
            O = N.split("E5")[1]
            T = O.split()[0]
            E = '5' + f"{T}"
        if 'E6' in N:
            O = N.split("E6")[1]
            T = O.split()[0]
            E = '6' + f"{T}"
        if 'E7' in N:
            O = N.split("E7")[1]
            T = O.split()[0]
            E = '7' + f"{T}"
        if 'E8' in N:
            O = N.split("E8")[1]
            T = O.split()[0]
            E = '8' + f"{T}"
        if 'E9' in N:
            O = N.split("E9")[1]
            T = O.split()[0]
            E = '9' + f"{T}"
        if E:
            e = E.replace("E", " ")
            n = N.split(f"{E}")[0]
        if not E:
            D = m.replace("720P", " ")
            if "20" in D:
                f = D.split("20")[0]
                U = D.split("20")[1]
                K = U.split()[0]
                Y = '20' + f"{K}"
            if "19" in D:
                f = D.split("19")[0]
                U = D.split("19")[1]
                K = U.split()[0]
                Y = '19' + f"{K}"
        if Y:
            YR = f"\n👌سال: {Y}"
        else:
            YR = f"\n👌سال:"
        if Q:
            q = f"\n🔷کیفیت: {Q}"
        if E:
            await message.edit(f"♨️سریال: ({n}) \n👌قسمت: {e} {q} \n🔻تماشای آنلاین بدون فیلتر شکن: \n🆔👉 @dlmacvin_new")
        else:
            await message.edit(f"♨️فیلم: ({f} {Y}) {YR} {q} \n🔻تماشای آنلاین بدون فیلتر شکن: \n🆔👉 @dlmacvin_new")
