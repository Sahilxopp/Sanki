from typing import Union
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from SankiMusic.utilities.config import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="Cᴏᴍᴍᴀɴᴅs",
                url=f"https://t.me/{BOT_USERNAME}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text="Sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            )
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="Hᴇʟᴘ", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="Uᴘᴅᴀᴛᴇs", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="Sᴜᴘᴘᴏʀᴛ", url=config.SUPPORT_GROUP
            )
        ],
        [    
            InlineKeyboardButton(
                text="Sᴏᴜʀᴄᴇ", url="https://te.legra.ph/file/d1ac5371d520226e87afa.mp4"
            ),
            InlineKeyboardButton(
                text="Oᴡɴᴇʀ", user_id=OWNER
            )
        ]
     ]
    return buttons
