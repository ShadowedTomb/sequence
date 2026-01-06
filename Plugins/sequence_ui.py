
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Database.sequence_prefs import toggle
from pyrogram import Client, filters

@Client.on_callback_query(filters.regex("^sequence_"))
async def sequence_handler(client, callback_query):
    await callback_query.answer("OK")

def buttons():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🎬 Episode", callback_data="seq_episode"),
            InlineKeyboardButton("📦 Season", callback_data="seq_season"),
        ],
        [
            InlineKeyboardButton("🎞 Quality", callback_data="seq_quality"),
        ]
    ])

@app.on_message(filters.command("sequence"))
async def sequence_ui(client, message):
    await message.reply("Choose sequence format:", reply_markup=buttons())

@app.on_callback_query(filters.regex("^seq_"))
async def seq_toggle(client, cb):
    key = cb.data.replace("seq_","")
    toggle(cb.from_user.id, f"use_{key}")
    await cb.answer("Updated")
