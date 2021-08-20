from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait

@Client.on_message(filters.media & filters.channel)
async def caption(client, message: Message):
    media = message.video or message.document
    if (media is not None) and (media.file_name is not None):
        m = media.file_name.replace("Fragmanı", "").replace("Fragmanlarım", "").replace("ı", "i").replace("İ", "I").replace("ö", "o").replace("Ö", "O").replace("Ü", "U").replace("ü", "u").replace("ë", "e").replace("Ë", "E").replace("Ä", "A").replace("ç", "c").replace("Ç", "C").replace("ş", "s").replace("Ş", "S").replace("ğ", "g").replace("Ğ", "G").replace("ä", "a")
        D = m.replace("720P", "").replace("E20", "").replace("E120", "").replace("E220", "").replace("E320", "")
        N = m.replace("@dlmacvin2 -", "").replace("@dlmacvin -", "")
        Z = media.file_name
        fa = " "
        X = " "
        tz = " "
        Lo = " "
        if "Sen Cal Kapimi" in m:
            fa += "#تو_در_خانه_ام_را_بزن"
            X += "Sen Cal Kapimi"
            Kh = m.replace("Sen Cal Kapimi", "")
        if "Marasli" in m:
            fa += "#اهل_ماراش"
            X += "Marasli"
        if "Sibe Mamnooe" in m:
            fa += "#سیب_ممنوعه"
            X += "Sibe Mamnooe"

        if Z.__contains__("Fragman"):
            Jn = m.split("Bolum")[1]
            if "2" in Jn:
                tz += "#دوم"
            elif "1" in Jn:
                tz += "#اول"
            elif "3" in Jn:
                tz += "#سوم"
            elif "4" in Jn:
                tz += "#چهارم"
            elif "5" in Jn:
                tz += "#پنجم"
            elif "6" in Jn:
                tz += "#ششم"
            if X.__contains__("a") or X.__contains__("o") or X.__contains__("i") or X.__contains__("c") or X.__contains__("b") or X.__contains__("e") or X.__contains__("l") or X.__contains__("n") or X.__contains__("m"):
                Yd = X.replace(" ", "_")
                Lo += "#" + f"{Yd}"
                V = Kh.split("Bolum")[0]
                E = V.replace(".", "")
            else:
                E = ""
            Tzz = tz.replace("#", "")
            date = "پنجشنبه ساعت 4 بامداد از رسانه اینترنتی دی ال مکوین"
            await message.edit(f"⬇️ تیزر{Tzz} قسمت {E} ({fa} ) {Lo} ، بازیرنویس چسبیده\n\n🔻 پخش {date}\n\n🆔👉 @dlmacvin_new")
        if (media.file_size > 50) and N.__contains__("E0") or N.__contains__("E1") or N.__contains__("E2") or N.__contains__("E3") or N.__contains__("E4") or N.__contains__("E5") or N.__contains__("E6") or N.__contains__("E7") or N.__contains__("E8") or N.__contains__("E9"):
            if '720P' in m:
                Q = '720'
            if '480P' in m:
                Q = '480'
            if '1080P' in m:
                Q = '1080'
            if '240P' in m:
                Q = '240'
            if Q:
                q = f"\n🔹کیفیت : {Q}"
            else:
                q = ""
            if 'E0' in N:
                O = N.split("E0")[1]
                T = O.split()[0]
                E = '0' + f"{T}"
                n = N.split("E0")[0]
            if 'E1' in N:
                O = N.split("E1")[1]
                T = O.split()[0]
                E = '1' + f"{T}"
                n = N.split("E1")[0]
            if 'E2' in N:
                O = N.split("E2")[1]
                T = O.split()[0]
                E = '2' + f"{T}"
                n = N.split("E2")[0]
            if 'E3' in N:
                O = N.split("E3")[1]
                T = O.split()[0]
                E = '3' + f"{T}"
                n = N.split("E3")[0]
            if 'E4' in N:
                O = N.split("E4")[1]
                T = O.split()[0]
                E = '4' + f"{T}"
                n = N.split("E4")[0]
            if 'E5' in N:
                O = N.split("E5")[1]
                T = O.split()[0]
                E = '5' + f"{T}"
                n = N.split("E5")[0]
            if 'E6' in N:
                O = N.split("E6")[1]
                T = O.split()[0]
                E = '6' + f"{T}"
                n = N.split("E6")[0]
            if 'E7' in N:
                O = N.split("E7")[1]
                T = O.split()[0]
                E = '7' + f"{T}"
                n = N.split("E7")[0]
            if 'E8' in N:
                O = N.split("E8")[1]
                T = O.split()[0]
                E = '8' + f"{T}"
                n = N.split("E8")[0]
            if 'E9' in N:
                O = N.split("E9")[1]
                T = O.split()[0]
                E = '9' + f"{T}"
                n = N.split("E9")[0]
            if not "Hard-Sub" in N:
                H = fa.replace("_", " ").replace("#", " ")
                await message.edit(f"🔺{H} قسمت {E} \n🔸 دوبله فارسی {q} \n🆔👉 @dlmacvin_new | {fa}")
            else:
                if message.video:
                    await message.edit(f"♨️ سریال{fa} ( {n}) بازیرنویس چسبیده\n👌قسمت: {E} {q} \n🔻تماشای آنلاین بدون فیلتر شکن: \n🆔👉 @dlmacvin_new")
                else:
                    await message.edit(f"♨️ سریال{fa} ({n}) بازیرنویس چسبیده\n👌قسمت: {E} {q} \n🔻تماشای آنلاین بدون فیلتر شکن: \n🆔👉 @dlmacvin_new")
        elif (media.file_size > 50) and not N.__contains__("E0") or N.__contains__("E1") or N.__contains__("E2") or N.__contains__("E3") or N.__contains__("E4") or N.__contains__("E5") or N.__contains__("E6") or N.__contains__("E7") or N.__contains__("E8") or N.__contains__("E9"):
            if "20" in D:
                f = D.split("20")[0]
                U = D.split("20")[1]
                K = U.split()[0]
                Y = '20' + f"{K}"
                YR = f"\n👌سال : {Y}"
            if "19" in D:
                f = D.split("19")[0]
                U = D.split("19")[1]
                K = U.split()[0]
                Y = '19' + f"{K}"
                YR = f"\n👌سال : {Y}"
            W = "20" or "19"
            if not W in D:
                P = m.split("0P")[0]
                f = P.replace("72", "").replace("48", "").replace("108", "").replace("24", "")
                YR = f"\n👌سال :"
            if '720P' in m:
                Q = '720'
            if '480P' in m:
                Q = '480'
            if '1080P' in m:
                Q = '1080'
            if '240P' in m:
                Q = '240'
            if Q:
                G = f"\n🔹کیفیت : {Q}"
                q = G.replace(".1", " ").replace(".mkv", " ")
            else:
                q = ""
            await message.edit(f"♨️ فیلم {f} بازیرنویس چسبیده{YR} {q} \n🔻تماشای آنلاین بدون فیلتر شکن: \n🆔👉 @dlmacvin_new")
