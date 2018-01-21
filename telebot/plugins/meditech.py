import os
from telebot import emojies

PARDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
IMG = PARDIR + '/imgs/meditech.png'


def handle(bot, update):
    msg = '{} Test ! Meditech JSC {}' . format(emojies.fire, emojies.fire)
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg)
    bot.send_sticker(chat_id=update.message.chat_id,
                     caption='Meditech',
                     sticker=open(IMG, 'rb'))
    return
