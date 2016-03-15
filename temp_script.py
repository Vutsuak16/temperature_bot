__name__ = "vutsuak"

from telegram import Updater
from telegram.error import Unauthorized
import serial


updater = Updater(token='199517321:AAEBVPSIGu7kt4aYMe_hi_3i2YRfniZAZME')

dispatcher = updater.dispatcher


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Wanna know room temperature??")


dispatcher.addTelegramCommandHandler('start', start)


def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="No such command")


dispatcher.addUnknownTelegramCommandHandler(unknown)


def yes(bot, update, args):
    temp=0
    ct=0
    ser = serial.Serial('COM7', 9600)
    while ct!=5:
        temp=(ser.readline())
        print temp
        ct+=1
    bot.sendMessage(chat_id=update.message.chat_id, text=temp+" Centigrade")


dispatcher.addTelegramCommandHandler('yes', yes)

updater.start_polling()
