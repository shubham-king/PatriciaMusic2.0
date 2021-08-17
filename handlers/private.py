from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn, BOT_USERNAME as bu 
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo("https://telegra.ph/file/638627c193ab240adb930.jpg")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎀
I Cᴀɴ Pʟᴀʏ Mᴜsɪᴄ Iɴ Yᴏᴜʀ Sᴇxʏ Gʀᴏᴜᴩ Vᴏɪᴄᴇ Cʜᴀᴛ. Dᴇᴠᴇʟᴏᴩᴇᴅ Bʏ [ShubhamMusics](https://t.me/ShubhamMusics).
Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴩ Aɴᴅ Pʟᴀʏ Mᴜsɪᴄ Fʀᴇᴇʟʏ!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "MUSIC GROU ", url="https://t.me/Music_Enviroment")
                  ],[
                    InlineKeyboardButton(
                        "Sᴜᴩᴩᴏʀᴛ👿", url="https://t.me/Robottech_chat"
                    ),
                    InlineKeyboardButton(
                        "Cʜᴀɴɴᴇʟ", url="https://t.me/ShubhamMusics"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add to Group➕", url="https://t.me/{bu}?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Aᴍ Oɴʟɪɴᴇ ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊Uᴩᴅᴀᴛᴇs", url="https://t.me/ShubhamMusics")
                ]
            ]
        )
   )
