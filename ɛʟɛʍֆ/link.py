from pyrogram import Client, filters, StopPropagation
from pyrogram.types import Message
from Trial import *
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    )

@Client.on_message(
    filters.group
    &filters.private
    &filters.command("link", prefixes='/')
                   ) 
async def love(_, ydl: Message):
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🍕𝗘𝗗𝗠🍕", url="https://t.me/")],
        [InlineKeyboardButton("🍤𝗟𝗼-𝗙𝗶🍤:", url="https://t.me/")],
        [InlineKeyboardButton("🍨𝗧𝗥𝗔𝗣.𝗕𝗘𝗔𝗧🍨:", url="https://t.me/")],
        [InlineKeyboardButton("🌭𝗡𝗖𝗦🌭:", url="https://t.me/")],
        [InlineKeyboardButton("🍪𝗣𝗢𝗣🍪:", url="https://t.me/")]
    ])
    await ydl.reply_photo(
        "https://telegra.ph/file/ed28706fff93c4a2956e5.jpg",
        reply_markup=joinButton,
        caption=youtube_ex
        )
    raise StopPropagation