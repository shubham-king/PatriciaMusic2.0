from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn, BOT_USERNAME as bu 
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo("https://telegra.ph/file/220461530b9b4cc13a7ab.jpg")
    await message.reply_text(
        f"""**ʜᴇʏ, ɪ 'ᴍ {bn} 🎀
ι αм α ρяσנє¢т σf ѕнυвнαм мυѕι¢  тσ ρℓαу ѕσиg ιи тєℓєgяαм gяσυρ/¢нαииєℓ νσι¢є ¢нαт Dᴇᴠᴇʟᴏᴩᴇᴅ Bʏ [ShubhamMusics](https://t.me/ShubhamMusics).
α∂∂ тσ уσυя gяσυρ αи∂ ρℓαу fяєєℓу!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝖒𝖚𝖘𝖎𝖈 𝖌𝖗𝖔𝖚𝖕 ", url="https://t.me/Music_Enviroment")
                  ],[
                    InlineKeyboardButton(
                        "𝖘𝖚𝖕𝖕𝖔𝖗𝖙", url="https://t.me/Robottech_chat"
                    ),
                    InlineKeyboardButton(
                        "𝖈𝖍𝖆𝖓𝖓𝖊𝖑", url="https://t.me/ShubhamMusics"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ 𝖆𝖉𝖉 𝖙𝖔 𝖌𝖗𝖔𝖚𝖕 ➕", url="https://t.me/IntelMusic_Gobot?startgroup=true"
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
