from pyrogram import Client, filters

import youtube_dl
from youtube_search import YoutubeSearch
import requests

import os
import time
from config import Config
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Dvp="Developer"
APPER="MASTER🔍"
OWNER="Other Bots 🙂"
GITCLONE="https://t.me/mhdfajisn"
B2="telegram.dog/mhdfajis"
BUTTON1="MASTER🔍"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 10 ** i for i, x in enumerate(reversed(stringt.split(':'))))

@Client.on_message(filters.command(['start'])) 
async def start(client, message):
    await message.reply_photo(photo=Config.START_IMG, caption=Config.START_MSG.format(message.from_user.mention),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(BUTTON1, url=GITCLONE)
                 ],[
                    InlineKeyboardButton(OWNER,url=f"https://t.me/fnm_bots"),
                    InlineKeyboardButton(Dvp, url=B2)
            ]
          ]
        ),
        reply_to_message_id=message.message_id
    )


@Client.on_message(filters.command(['song']))
def a(client, message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply('`Searching... ...For {message}🔍`')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]
            views = results[0]["views"]

            ## UNCOMMENT THIS IF YOU WANT A LIMIT ON DURATION. CHANGE 1800 TO YOUR OWN PREFFERED DURATION AND EDIT THE MESSAGE (30 minutes cap) LIMIT IN SECONDS
            # if time_to_seconds(duration) >= 7000:  # duration limit
            #     m.edit("Exceeded 30mins cap")
            #     return

            performer = f"@mhdfajis/🇮🇳" 
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            print(e)
            m.edit('**👎 Nothing found Retry with another !**')
            return
    except Exception as e:
        m.edit(
            "**Enter Song Name with /song Command!**"
        )
        print(str(e))
        return
    m.edit("**Found Your Song 🎵, Trying  To Upload To Telegram it will takes upto 1 minute...**")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 1%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 3%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 6%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 9%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 12%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 15%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 18%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 21%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 24%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 27%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 30%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 33%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 36%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 39%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 42%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 45%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 48%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 51%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 54%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 57%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 60%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 63%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 66%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 69%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 72%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 75%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 78%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 81%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 84%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 87%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 90%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 93%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 96%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 99%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 99.98%")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 99.99")
    m.edit("⚙️ Status: 📥 Downloading 📥 : 100")
    m.edit("⚙️ Status: Uploading : 1%")
    m.edit("⚙️ Status: Uploading : 3%")
    m.edit("⚙️ Status: Uploading : 6%")
    m.edit("⚙️ Status: Uploading : 9%")
    m.edit("⚙️ Status: Uploading : 12%")
    m.edit("⚙️ Status: Uploading : 15%")
    m.edit("⚙️ Status: Uploading : 18%")
    m.edit("⚙️ Status: Uploading : 21%")
    m.edit("⚙️ Status: Uploading : 24%")
    m.edit("⚙️ Status: Uploading : 27%")
    m.edit("⚙️ Status: Uploading : 30%")
    m.edit("⚙️ Status: Uploading : 33%")
    m.edit("⚙️ Status: Uploading : 36%")
    m.edit("⚙️ Status: Uploading : 39%")
    m.edit("⚙️ Status: Uploading: 42%")
    m.edit("⚙️ Status: Uploading : 45%")
    m.edit("⚙️ Status: Uploading : 48%")
    m.edit("⚙️ Status: Uploading : 51%")
    m.edit("⚙️ Status: Uploading: 54%")
    m.edit("⚙️ Status: Uploading : 57%")
    m.edit("⚙️ Status: Uploading : 60%")
    m.edit("⚙️ Status: Uploading : 63%")
    m.edit("⚙️ Status: Uploading : 66%")
    m.edit("⚙️ Status: Uploading : 69%")
    m.edit("⚙️ Status: Uploading : 72%")
    m.edit("⚙️ Status: Uploading : 75%")
    m.edit("⚙️ Status: Uploading : 78%")
    m.edit("⚙️ Status: Uploading : 81%")
    m.edit("⚙️ Status: Uploading : 84%")
    m.edit("⚙️ Status: Uploading : 87%")
    m.edit("⚙️ Status: Uploading : 90%")
    m.edit("⚙️ Status: Uploading : 93%")
    m.edit("⚙️ Status: Uploading : 96%")
    m.edit("⚙️ Status: Uploading : 99%")
    m.edit("⚙️ Status: Uploading : 99.98%")
    m.edit("⚙️ Status: Uploading : 99.99")
    m.edit("⚙️ Status: Uploading : 100")
    
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'🎶 <b>Title:</b> <a href="{link}">{title}</a>\n⌚ <b>Duration:</b> <code>{duration}</code>\n📻 <b>Uploaded By:</b> <a href="https://t.me/Fajis_SongBot">Fajis Song Bot</a>'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, parse_mode='HTML',quote=False, title=title, duration=dur, performer=performer, thumb=thumb_name)
        m.delete()
    except Exception as e:
        m.edit('**An internal Error Occured, Report This @mhdfajis!!**')
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
