from distutils.archive_util import make_archive
from telebot import types

def create_keyboard(keys, row_width=2, resize_keyboard=True, emojize=True):
    markup = types.ReplyKeyboardMarkup(row_width=row_width, resize_keyboard=resize_keyboard)
    buttons = list(map(types.KeyboardButton, keys))
    markup.add(*buttons)
    return markup