# قناتي السورس : @moussa_pro
#مجموعة السورس : @moussa_pro_groop
# مجموعة MOUSSA LIGHTNING الرسمية : @MOUSSA_Lightning
#معرف المطور : @u_5_1
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins

# uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/d1bf6a7e7998469ea80fb.mp4"
pm_caption = "KITNI SEXY H YRR`\n\n"

@borg.on(admin_cmd(pattern=r"سكسي"))
async def friday(alive):
    chat = await alive.get_chat()
    """ ارسل الامر  .سكسي  ,للتأكد من حالة عمل البوت.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()

    
@borg.on(admin_cmd(pattern=r"اسطورة", allow_sudo=True))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
