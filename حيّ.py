import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events
from userbot.utils import admin_cmd, sudo_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "〖 𝕄𝕆𝕌𝕊𝕊𝔸 〗𓆩ℙℝ𝕆𓆪"
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO" , None)

global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/6aa39732748ed7c319943.jpg"
file2 = "https://telegra.ph/file/a6d72504bc09e71484a54.jpg"
file3 = "https://telegra.ph/file/3cdbede1d5d85aa2d50fc.jpg"
file4 = "https://telegra.ph/file/3dae01973943e8b28c931.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "****\n\n"
pm_caption += "**نعم سيدي ، أنا على قيد الحياة والأنظمة تعمل بشكل مثالي كما ينبغي لها أن تعمل...**\n\n"
pm_caption += "✘ About My System ✘\n\n"
pm_caption += "➾ **اصدار تليثون** ☞ 1.17.5\n"
pm_caption += "➾ **قناة البوت** ☞ [ᴊᴏɪɴ](https://t.me/MOUSSA_PRO)\n"
pm_caption += "➾ **ʟɪᴄᴇɴꜱᴇ**  ☞ [〖 𝕄𝕆𝕌𝕊𝕊𝔸 〗𓆩ℙℝ𝕆𓆪](https://github.com/DARK-COBRA)\n"
pm_caption += "➾ **ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ** ☞ [〖 𝕄𝕆𝕌𝕊𝕊𝔸 〗𓆩ℙℝ𝕆𓆪](https://github.com/DARK-COBRA/DARKCOBRA)\n\n"
pm_caption += f"➾ **ᴍʏ ᴍᴀsᴛᴇʀ** ☞ [{DEFAULTUSER}](tg://user?id={ghanti})\n"

@borg.on(admin_cmd(pattern=r"بوت"))

async def amireallyalive(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    await alive.delete()
    
    """ استخدام الأمر .بوت, للتأكد من حالة عمل البوت.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@borg.on(admin_cmd(outgoing=True, pattern="بوت2"))
async def amireallyalive(alive):
    """استخدم الأمر .بوت2,للتأكد من حالة عمل البوت.  """
    if ALIVE_PHOTTO:
        pm_caption = "**〖 𝕄𝕆𝕌𝕊𝕊𝔸 〗𓆩ℙℝ𝕆𓆪 𝙸𝚂 🅾︎🅽🅻🅸🅽🅴**\n"
        pm_caption += f"**𝕄𝕪 𝔹𝕠𝕤𝕤**            : {DEFAULTUSER}\n"
        pm_caption += "إصدار تليثون        : 1.17.5\n"
        pm_caption += "إصدار بايثون          : 3.9.0\n"
        pm_caption += "قناة البوت         : [ᴊᴏɪɴ](https://t.me/moussa_pro)\n"
        pm_caption += "مجموعة البوت           : [ᴊᴏɪɴ](https://t.me/moussa_pro_group)\n"
        pm_caption += "𝘓𝘐𝘚𝘌𝘕𝘊𝘌                  : [AGPL-3.0  ʟɪᴄᴇɴꜱᴇ](https://jenaatul8.wixsite.com/hellboi-atul)\n"
        pm_caption += "𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔            : [ 〖 𝕄𝕆𝕌𝕊𝕊𝔸 〗𓆩ℙℝ𝕆𓆪 ](https://t.me/MOUSSA_PRO)\n"
        pm_caption += "[┏┓━┏┓━━━━┏┓━┏┓━━━━━\n ┃┃━┃┃━━━━┃┃━┃┃━━━━━\n ┃┗━┛┃┏━━┓┃┃━┃┃━┏━━┓\n ┃┏━┓┃┃┏┓┃┃┃━┃┃━┃┏┓┃ \n ┃┃━┃┃┃┃━┫┃┗┓┃┗┓┃┗┛┃ \n ┗┛━┗┛┗━━┛┗━┛┗━┛┗━━┛](https://t.me/MOUSSA_PRO_group)"
        chat = await alive.get_chat()
        await alive.delete()
        """ استخدام الأمر .بوت3 ,للتأكد من حالة عمل البوت .  """
        await borg.send_file(alive.chat_id, ALIVE_PIC,caption=pm_caption, link_preview = False)
        await allive.delete()
        return
    req = requests.get("https://telegra.ph/file/6d067b1a626a25735f5ed.png")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_file(alive.chat_id, file=sticker)
        await borg.send_message(alive.chat_id,"**〖 𝕄𝕆𝕌𝕊𝕊𝔸 〗𓆩ℙℝ𝕆𓆪 𝙸𝚂 🅾︎🅽🅻🅸🅽🅴**\n"
                      f"**𝕄𝕪 𝔹𝕠𝕤𝕤**            : {DEFAULTUSER}\n"
                      "اصدار تليثون        : 1.17.5\n"
                      "اصدار بايثون          : 3.9.0\n"
                      "قناة البوت         : [ᴊᴏɪɴ](https://t.me/moussa_pro)\n"
                      "مجموعة البوت           : [ᴊᴏɪɴ](https://t.me/moussa_pro_group)\n"
                      "𝘓𝘐𝘚𝘌𝘕𝘊𝘌                  : [AGPL-3.0  ʟɪᴄᴇɴꜱᴇ](https://jenaatul8.wixsite.com/hellboi-atul)\n"
                      "𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔            : [ 〖 𝕄𝕆𝕌𝕊𝕊𝔸 〗𓆩ℙℝ𝕆𓆪 ](https://t.me/MOUSSA_PRO)\n"
                                "[ ┏┓━┏┓━━━━┏┓━┏┓━━━━━\n ┃┃━┃┃━━━━┃┃━┃┃━━━━━\n ┃┗━┛┃┏━━┓┃┃━┃┃━┏━━┓\n ┃┏━┓┃┃┏┓┃┃┃━┃┃━┃┏┓┃ \n ┃┃━┃┃┃┃━┫┃┗┓┃┗┓┃┗┛┃ \n ┗┛━┗┛┗━━┛┗━┛┗━┛┗━━┛](https://t.me/MOUSSA_PRO)" , link_preview = False) 
        await alive.delete()
