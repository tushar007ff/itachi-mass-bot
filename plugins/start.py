import os
import sys
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from info import Config, Txt


@Client.on_message(filters.private & filters.command('start'))
async def handle_start(bot:Client, message:Message):

    Btn = [
        [InlineKeyboardButton(text='🔥𝐻𝑒𝑙𝑝 𝑎𝑛𝑑 𝑐𝑜𝑚𝑚𝑎𝑛𝑑𝑠🔥', callback_data='help')],
        [InlineKeyboardButton(text='✨𝐔𝐏𝐃𝐀𝐓𝐄𝐒✨', url='https://t.me/TFW_UPDATES'), InlineKeyboardButton(text='🔮𝐒𝐔𝐏𝐏𝐎𝐑𝐓🔮', callback_data='about')]
        ]

    await message.reply_text(photo="https://files.catbox.moe/k2m8xl.jpg", text=Txt.START_MSG.format(message.from_user.mention), reply_markup=InlineKeyboardMarkup(Btn))


#Restart to cancell all process 
@Client.on_message(filters.private & filters.command("r") & filters.user(Config.SUDO) & filters.user(Config.OWNER))
async def restart_bot(b, m):
    await m.reply_text("🔄__𝗒𝗈𝗎𝗋 𝖻𝗈𝗍 𝗌𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅 𝗋𝖾𝗌𝗍𝖺𝗋𝗍.....__")
    os.execl(sys.executable, sys.executable, *sys.argv)
