from telegram.ext import Updater, CommandHandler
import logging

TOKEN='776745027:AAGnaz4ngF2679aJUJBIXCr5Z0fbR_g0rFs'
REQUEST_KWARGS={
    'proxy_url': 'http://192.168.13.1:3128/',
    # Optional, if you need authentication:
    #'username': 'PROXY_USER',
    #'password': 'PROXY_PASS',
}

updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS)
logging.basicConfig(level=logging.INFO)


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


def t(bot, update):
    update.message.reply_text(
        'tua madre {}'.format(update.message.from_user.first_name)
    )


def ripeti(bot, update):
    update.message.reply_text(
        '{}'.format(update.message.text)
    )


updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('t', t))
updater.dispatcher.add_handler(CommandHandler('ripeti', ripeti))

if __name__ == "__main__":
    updater.start_polling()
    updater.idle()
