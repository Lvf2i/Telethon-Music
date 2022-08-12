import os

from telethon import Button, events, types
from R0R77.status import *
from R0R77 import *


PINS_TEXT = """
**✘ اوامر تثبيت والغاء التثبيت لرسائل في المجموعة**

‣ `!تثبيت`
بالرد على الرسالة التي تريد تثبيتها

‣ `!الغاء تثبيت`
بالرد على الرسالت التي تريد الغاء تثبيتها

‣ `!الغاء التثبيت للكل`
لالغاء تثبيبت جميع الرسائل في المجموعة

‣ `!الرسائل المثبتة`
لأظهار الرسائل المثبتة في المجموعة

@meeddu
"""

@R0R77.on(events.NewMessage(pattern="^[?!/]الرسائل المثبتة"))
async def get_pinned(event):
    chat_id = (str(event.chat_id)).replace("-100", "")

    Ok = await R0R77.get_messages(event.chat_id, ids=types.InputMessagePinned()) 
    tem = f"الرسائل المثبتة في الدردشة{event.chat.title} هي <a href=https://t.me/c/{chat_id}/{Ok.id}>here</a>."
    await event.reply(tem, parse_mode="html", link_preview=False)

@R0R77.on(events.NewMessage(pattern="^[!?/]تثبيت ?(.*)"))
@is_admin
async def pin(event, perm):
    if not perm.pin_messages:
       await event.reply("يجب ان تمتلك صلاحيات التثببيت اولا")
       return
    msg = await event.get_reply_message()
    if not msg:
       await event.reply("يجب عليك الرد على الرسالة اولا")
       return
    input_str = event.pattern_match.group(1)
    if "notify" in input_str:
       await R0R77.pin_message(event.chat_id, msg, notify=True)
       return
    await R0R77.pin_message(event.chat_id, msg)   

@R0R77.on(events.NewMessage(pattern="^[!?/]الغاء تثبيت ?(.*)"))
@is_admin
async def unpin(event, perm):
    if not perm.pin_messages:
       await event.reply("يجب ان تمتلك صلاحيات التثببيت اولا")
       return
    chat_id = (str(event.chat_id)).replace("-100", "")
    ok = await R0R77.get_messages(event.chat_id, ids=types.InputMessagePinned())
    await R0R77.unpin_message(event.chat_id, ok)
    await event.reply(f"تم بنجاح الغاء التثبيت [لهذه الرسالة](t.me/{event.chat.username}/{ok.id}).", link_preview=False)


@R0R77.on(events.NewMessage(pattern="^[!?/]الغاء التثبيت للكل$"))
async def unpinall(event, perm):
    if not perm.pin_messages:
       await event.reply("يجب ان تمتلك صلاحيات التثببيت اولا")
       return
    UNPINALL = """
هل انت متأكد من الغاء تثبيت الرسائل ؟
"""

    await R0R77.send_message(event.chat_id, UNPINALL, buttons=[
    [Button.inline("تأكيد", data="unpin")], 
    [Button.inline("الغاء", data="cancel")]])

@R0R77.on(events.callbackquery.CallbackQuery(data="unpin"))
async def confirm(event):
    check = await event.client.get_permissions(event.chat_id, event.sender_id)
    if check.is_creator:
        await R0R77.unpin_message(event.chat_id)
        await event.edit("تم بنجاح الغاء تثببيت جميع الرسائل")
        return 

    await event.answer("يجب ان تكون مالك المجموعة اولا")

@R0R77.on(events.callbackquery.CallbackQuery(data="cancel"))
async def cancel(event):

    check = await event.client.get_permissions(event.chat_id, event.sender_id)
    if check.is_creator:
        await event.edit("عملية الغاء تثبيت جميع الرسائل تم الغائها ")
        return 

    await event.answer("يجب ان تكون مالك المجموعة اولا")


@R0R77.on(events.callbackquery.CallbackQuery(data="pins"))
async def _(event):

    await event.edit(PINS_TEXT, buttons=[[Button.inline("رجوع", data="help")]])
