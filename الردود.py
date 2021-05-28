import asyncio
import re
from telethon import events, utils
from telethon.tl import types
from userbot.plugins.sql_helper.filter_sql import get_filter, add_filter, remove_filter, get_all_filters, remove_all_filters
from userbot import CMD_HELP

DELETE_TIMEOUT = 0
TYPE_TEXT = 0
TYPE_PHOTO = 1
TYPE_DOCUMENT = 2


global last_triggered_filters
last_triggered_filters = {}  # pylint:disable=E0602


@command(incoming=True)
async def on_snip(event):
    global last_triggered_filters
    name = event.raw_text
    if event.chat_id in last_triggered_filters:
        if name in last_triggered_filters[event.chat_id]:
            # avoid userbot spam
            # "I demand rights for us bots, we are equal to you humans." -Henri Koivuneva (t.me/MOUSSA_PRO/2698)
            return False
    snips = get_all_filters(event.chat_id)
    if snips:
        for snip in snips:
            pattern = r"( |^|[^\w])" + re.escape(snip.keyword) + r"( |$|[^\w])"
            if re.search(pattern, name, flags=re.IGNORECASE):
                if snip.snip_type == TYPE_PHOTO:
                    media = types.InputPhoto(
                        int(snip.media_id),
                        int(snip.media_access_hash),
                        snip.media_file_reference
                    )
                elif snip.snip_type == TYPE_DOCUMENT:
                    media = types.InputDocument(
                        int(snip.media_id),
                        int(snip.media_access_hash),
                        snip.media_file_reference
                    )
                else:
                    media = None
                message_id = event.message.id
                if event.reply_to_msg_id:
                    message_id = event.reply_to_msg_id
                await event.reply(
                    snip.reply,
                    file=media
                )
                if event.chat_id not in last_triggered_filters:
                    last_triggered_filters[event.chat_id] = []
                last_triggered_filters[event.chat_id].append(name)
                await asyncio.sleep(DELETE_TIMEOUT)
                last_triggered_filters[event.chat_id].remove(name)


@command(pattern="^حفظ رد (.*)")
async def on_snip_save(event):
    name = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if msg:
        snip = {'type': TYPE_TEXT, 'text': msg.message or ''}
        if msg.media:
            media = None
            if isinstance(msg.media, types.MessageMediaPhoto):
                media = utils.get_input_photo(msg.media.photo)
                snip['type'] = TYPE_PHOTO
            elif isinstance(msg.media, types.MessageMediaDocument):
                media = utils.get_input_document(msg.media.document)
                snip['type'] = TYPE_DOCUMENT
            if media:
                snip['id'] = media.id
                snip['hash'] = media.access_hash
                snip['fr'] = media.file_reference
        add_filter(event.chat_id, name, snip['text'], snip['type'], snip.get('id'), snip.get('hash'), snip.get('fr'))
        await event.edit(f"الرد {name} تم إضافته. جربه الآن {name}")
    else:
        await event.edit("Reply to a message with `savefilter keyword` to save the filter")


@command(pattern="^.الردود$")
async def on_snip_list(event):
    all_snips = get_all_filters(event.chat_id)
    OUT_STR = "Available Filters in the Current Chat:\n"
    if len(all_snips) > 0:
        for a_snip in all_snips:
            OUT_STR += f"👉 {a_snip.keyword} \n"
    else:
        OUT_STR = "لا يوجد ردود محفوظة. يمكنك استخدام الأمر `.حفظ رد` لحفظ ردود جديدة"
    if len(OUT_STR) > 4096:
        with io.BytesIO(str.encode(OUT_STR)) as out_file:
            out_file.name = "filters.text"
            await bot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="المعذرة. لم يتم العثور على ردود في هذه المحادثة",
                reply_to=event
            )
            await event.delete()
    else:
        await event.edit(OUT_STR)


@command(pattern="^حذف رد (.*)")
async def on_snip_delete(event):
    name = event.pattern_match.group(1)
    remove_filter(event.chat_id, name)
    await event.edit(f"الرد {name} تم حذفه")


@command(pattern="^.حذف ردود$")
async def on_all_snip_delete(event):
    remove_all_filters(event.chat_id)
    await event.edit(f"الردود **in current chat** تم حذفها جميعاً")

CMD_HELP.update(
    {
        "filters": "__**PLUGIN NAME :** filters__\
    \n\n📌** CMD ★** `.حفظ رد (text/filter key) (reply to msg)`\
    \n**USAGE   ★  **save ur filter in chat when someone type that key it reply with the msg u put on reply (note:-it activate only when someone reply not u. \
    \n\n📌** CMD ★** `.الردود`\
    \n**USAGE   ★  **list all ur filters in a chat\
    \n\n📌** CMD ★** `.حذف رد(key/text)`\
    \n**USAGE   ★  **stop the filter u put on the key\
    \n\n📌** CMD ★** `.حذف ردود`\
    \n**USAGE   ★  **clear all ur filters"
    }
)
