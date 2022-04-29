import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/c6e1041c6c9a12913f57a.png",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 𝐇𝐞𝐥𝐥𝐨, 𝐈 𝐚𝐦 𝐒𝐮𝐩𝐞𝐫𝐟𝐚𝐬𝐭 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲
𝐍𝐨 𝐋𝐚𝐠 𝐕𝐂 𝐌𝐮𝐬𝐢𝐜 𝐏𝐥𝐚𝐲𝐞𝐫 𝐁𝐨𝐭.

┏━━━━━━━━━━━━━━━━━┓
┣★ 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 » [𝐒𝐡𝐨𝐧𝐚 𝐌𝐮𝐬𝐢𝐜](https://t.me/shonamusic)
┣★ 𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐁𝐲 : [𝐌𝐢𝐬𝐬 𝐒𝐡𝐨𝐧𝐚](https://t.me/Rasogolla8)
┣★ 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 ➪ : [𝐂𝐥𝐢𝐜𝐤~𝐇𝐞𝐫𝐞](https://t.me/kaalxd)
┣★ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 ➪ : [𝐂𝐥𝐢𝐜𝐤~𝐇𝐞𝐫𝐞](https://t.me/sscnewgroup)
┗━━━━━━━━━━━━━━━━━┛

💞 𝐉𝐮𝐬𝐭 𝐀𝐝𝐝 𝐌𝐞 » 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝
𝐄𝐧𝐣𝐨𝐲 𝐒𝐮𝐩𝐞𝐫 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 ❥︎𝐌𝐮𝐬𝐢𝐜.
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ❱ ➕", url=f"https://t.me/shonarobot?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/start@shonarobot", "/alive", "#Kaal"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/500f6bd88da241e0c694a.png",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐒𝐭𝐮𝐝𝐲 𝐆𝐫𝐨𝐮𝐩 💞", url=f"https://t.me/sanki_world")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/500f6bd88da241e0c694a.png",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 𝐂𝐥𝐢𝐜𝐤 𝐌𝐞 𝐓𝐨 𝐆𝐞𝐭 𝐑𝐞𝐩𝐨 💞", url=f"https://t.me/iamkaal")
                ]
            ]
        ),
    )
