from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["love"]), group=-2)
async def love(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("💋LOVE💋:", url="https://t.me/vrtxmusic")],
    ])
    Aww = f"""Hey <b>{message.from_user.first_name}</b>
If you liked my project and want to be a GitHub contributor then:
- 📧You may email me at **calitronvrtx@gmail.com**
- 📬You can personal message me in Telegram **@calitronx**   
- ✨Star & Fork my GitHub acct. and/or repo.\n

If you liked my project and want and just want to make me happy then you can:
- 🌹share my bot and make me happy 🌹
    
**<b>{message.from_user.first_name}</b> 😁Thanks a lot for using my bot🍰**

[ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ](https://telegra.ph/file/a532f298b920e99bd58bb.jpg)
"""      
    await message.reply_text(Aww, reply_markup=joinButton)
    raise StopPropagation
