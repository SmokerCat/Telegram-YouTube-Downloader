'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
from pyrogram import Client, filters, StopPropagation
from pyrogram.types import Message
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    )
from Trial import *
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
@Client.on_message(
    filters.command(
      "love",
      prefixes='/')) 
async def love(
    _,
    ydl: Message
    ):
  usrs = ydl.from_user.first_name
  joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton(
          "🍷 Gï†hµß:",
          url="https://github.com/calitronx?tab=repositories")]
        ])
  '🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
  Aww = f"""
🍟==========『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==========🍟

🎈Dear,
Sir,Ma'am  <b>**{usrs}**</b>

ɪꜰ ʏᴏᴜ ʟɪᴋᴇᴅ ᴍʏ ᴘʀᴏᴊᴇᴄᴛ ᴀɴᴅ ᴡᴀɴᴛ ᴛᴏ ʙᴇ ᴀ ɢɪᴛʜᴜʙ ᴄᴏɴᴛʀɪʙᴜᴛᴏʀ ᴛʜᴇɴ:
- 📧ʏᴏᴜ ᴍᴀʏ ᴇᴍᴀɪʟ ᴍᴇ ᴀᴛ `calitronvrtx@gmail.com`
- 📬ʏᴏᴜ ᴄᴀɴ ᴘᴇʀꜱᴏɴᴀʟ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ @calitronx  
- ✨ꜱᴛᴀʀ & ꜰᴏʀᴋ ᴍʏ ɢɪᴛʜᴜʙ ʀᴇᴘᴏ.

ɪꜰ ʏᴏᴜ ʟɪᴋᴇᴅ ᴍʏ ᴘʀᴏᴊᴇᴄᴛ ᴀɴᴅ ᴊᴜꜱᴛ ᴡᴀɴᴛ ᴛᴏ ᴍᴀᴋᴇ ᴍᴇ ꜱᴍɪʟᴇ ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ:
- 🌹 ꜱʜᴀʀᴇ ᴍʏ ʙᴏᴛꜱ @calitrox ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ʜᴀᴘᴘʏ 🌹
    
🍮 ᴛʜᴀɴᴋꜱ ᴀ ʟᴏᴛ ꜰᴏʀ ᴜꜱɪɴɢ ᴍʏ ʙᴏᴛ 🍮

🍟==========『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==========🍟
""" 
  '🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'     
  await ydl.reply_photo(
        youliurl,
        reply_markup=joinButton,
        caption=Aww
        )
  raise StopPropagation
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'