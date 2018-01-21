""" Show Meditech
"""
from telebot import emojies


def handle(bot, update):
    msg = '{0} Meditech JSC {1}' . format(emojies.fire, emojies.fire)
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg)
