from .. import Drone, ACCESS_CHANNEL
from telethon import events, Button
from LOCAL.localisation import START_TEXT as st
from LOCAL.localisation import JPG as file
from LOCAL.localisation import JPG4
from LOCAL.localisation import info_text, spam_notice, help_text, DEV, source_text, SUPPORT_LINK
from ethon.teleutils import mention

@Drone.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply(f'{st}', file=file,
                      buttons=[
                              [Button.inline("CONFIGURE", data="menu")]
                              ])
    tag = f'[{event.sender.first_name}](tg://user?id={event.sender_id})'
    await Drone.send_message(int(ACCESS_CHANNEL), f'{tag} started the BOT')
    
@Drone.on(events.callbackquery.CallbackQuery(data="menu"))
async def menu(event):
    await event.edit("**📑MENU.**",
                    buttons=[[
                         Button.inline("HELP", data="help"),
                         Button.inline("INFO", data="info")],
                         [
                         Button.inline("NOTE", data="notice"),
                         Button.url("DEV", url="t.me/shamilnelli")],
                         [
                         Button.url("UPDATES", url="t.me/mwkbots"),
                         Button.url("SUPPORT", url="t.me/redbullfed")]])
    
@Drone.on(events.callbackquery.CallbackQuery(data="info"))
async def info(event):
    await event.edit(f'**ℹ️ NFO:**\n\n{info_text}',
                    buttons=[[
                         Button.inline("HOME", data="menu")]])
    
@Drone.on(events.callbackquery.CallbackQuery(data="notice"))
async def notice(event):
    await event.answer(f'{spam_notice}', alert=True)
    
@Drone.on(events.callbackquery.CallbackQuery(data="source"))
async def source(event):
    await Drone.send_message(event.chat_id, source_text,
                    buttons=[[
                         Button.url("GITHUB.", url="https://github.com/Vasusen-code/VideoConvertor/tree/public")]])
                                    
    
@Drone.on(events.callbackquery.CallbackQuery(data="help"))
async def help(event):
    await event.edit('**🆘 HELP.**',
                    buttons=[[
                         Button.inline("FEATURES", data="plugins"),
                         Button.url("🐞 BUG", url="t.me/redbullfed")],
                         [
                         Button.inline("HOME", data="menu")]])
    
@Drone.on(events.callbackquery.CallbackQuery(data="plugins"))
async def plugins(event):
    await event.edit(f'{help_text}',
                    buttons=[[
                         Button.inline("HOME", data="menu")]])
    
    
    
    
    
