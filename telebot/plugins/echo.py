"""Echo plugin
/echo - Do nothing!
"""


def handle(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text='Hey! I\'m Meditech Bot')
