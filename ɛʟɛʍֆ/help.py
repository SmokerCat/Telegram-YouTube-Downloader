from pyrogram import Client, Filters

@Client.on_message(Filters.command(["help"]))
async def help(client, message):
    helptxt = f"""/help:[📥](https://telegra.ph/file/39812237fd7a1bfc02532.jpg)\n
                 .˜”*°•**InChat**•°*”˜.
Copy any Valid Youtube link and paste inside the bot and follow the prompts.
                 .˜”*°•**InGroups**•°*”˜.
Add me in any group then copy any valid Youtube link and paste inside the bot and follow the prompts.

                .📍**𝐈𝐌𝐏𝐎𝐑𝐓𝐀𝐍𝐓**📍.
-**♥ Bigger download size,more wait time ♥**
-𝐅𝐢𝐥𝐞 𝐬𝐢𝐳𝐞 𝐦𝐨𝐫𝐞 𝐭𝐡𝐞𝐧 𝟐𝐠𝐛 𝐰𝐨𝐧'𝐭 𝐛𝐞 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐝 𝐝𝐮𝐞 𝐭𝐨 𝐭𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐩𝐨𝐥𝐢𝐜𝐲."""
        
    
    await message.reply_text(helptxt)
