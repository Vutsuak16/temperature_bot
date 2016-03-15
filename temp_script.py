__name__ = "vutsuak"

from telegram import Updater
from telegram.error import Unauthorized
import serial


ser = serial.Serial('COM7', 9600)


updater = Updater(token='199517321:AAGX0Ylmxl5ainQ51QWQIGPVpwWasC19wYk')

dispatcher = updater.dispatcher


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Wanna know room temperature??")


dispatcher.addTelegramCommandHandler('start', start)


def unknown(bot, update):
        bot.sendMessage(chat_id=update.message.chat_id, text="No such command")


dispatcher.addUnknownTelegramCommandHandler(unknown)

def yes(bot, update, args):
    temp = str(ser.read())
    bot.sendMessage(chat_id=update.message.chat_id, text=temp)


dispatcher.addTelegramCommandHandler('yes', yes)




updater.start_polling()

