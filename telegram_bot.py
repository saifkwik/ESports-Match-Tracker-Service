from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import requests

updater = Updater("ENTER YOUR API KEY HERE",
                  use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Welcome to ESports Match Tracker telegram bot')


# max index is 15
def valo(update: Update, context: CallbackContext):
    url = "http://127.0.0.1:8000/valo?match_index=15"

    r = requests.get(url)
    val_api = r.json()
    for val in val_api:
        update.message.reply_text(f'{val[0]} : {val[1]}')


def cs(update: Update, context: CallbackContext):
    url = "http://127.0.0.1:8000/cs?match_index=15"

    r = requests.get(url)
    val_api = r.json()
    for val in val_api:
        update.message.reply_text(f'{val[0]} : {val[1]}')


def dota2(update: Update, context: CallbackContext):
    url = "http://127.0.0.1:8000/dota2?match_index=15"

    r = requests.get(url)
    val_api = r.json()
    for val in val_api:
        update.message.reply_text(f'{val[0]} : {val[1]}')


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
	/valo - To get Match list of valorant
	/cs - To get Match list of Counter Strike
	/dota2 - To get Match list of DOTA2""")


updater.dispatcher.add_handler(CommandHandler('valo', valo))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('cs', cs))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('dota2', dota2))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()

print('Telegram BOT running')
