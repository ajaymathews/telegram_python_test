import os
import glob
import time
import telegram
from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import serial
from threading import Thread
import warnings
warnings.filterwarnings("ignore")

def start(bot, update):
    print(update)
##    print("Sender:",update.message.chat.username)
##    print ("Current ChatID:",update.message.chat_id)
##    print("messageID",update.message.message_id)
##    print("")
    print("Connected to ",str(update.message.chat.username),"(",str(update.message.chat_id),")")
    print("Message Entered:'",(update.message.text),"'")
    print("")
    update.message.reply_text(str('Welcome '+str(update.message.chat.first_name)))
    custom_keyboard = [['/Button1','/Button2'],['/Button3','/Button4'],['/Button5','/Button6']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.sendMessage(update.message.chat_id,text='Choose Your Option',reply_markup=reply_markup)

  

#status function to call distance, temperature & humidity     
def Button1(bot, update):
    update.message.reply_text(str(update.message.chat.username)+" pressed Button1")
    print(str(update.message.chat.username)+" pressed Button1")

def Button2(bot,update):
    update.message.reply_text(str(update.message.chat.username)+" pressed Button2")
    print(str(update.message.chat.username)+" pressed Button2")

def Button3(bot, update):
    update.message.reply_text(str(update.message.chat.username)+" pressed Button3")
    print(str(update.message.chat.username)+" pressed Button3")

def Button4(bot, update):
    update.message.reply_text(str(update.message.chat.username)+" pressed Button4")
    print(str(update.message.chat.username)+" pressed Button4")

def Button5(bot, update):
    update.message.reply_text(str(update.message.chat.username)+" pressed Button5")
    print(str(update.message.chat.username)+" pressed Button5")

def Button6(bot, update):
    update.message.reply_text(str(update.message.chat.username)+" pressed Button6")
    print(str(update.message.chat.username)+" pressed Button6")

  


updater=Updater(token='627333566:AAGanhIPY2BP7UqOJcdAhjYR1mOJZG6OuyM') #'627333566:AAGanhIPY2BP7UqOJcdAhjYR1mOJZG6OuyM'
disp=updater.dispatcher

disp.add_handler(CommandHandler('start',start))
disp.add_handler(CommandHandler('Button1', Button1))
disp.add_handler(CommandHandler('Button2', Button2))
disp.add_handler(CommandHandler('Button3', Button3))
disp.add_handler(CommandHandler('Button4', Button4))
disp.add_handler(CommandHandler('Button5', Button5))
disp.add_handler(CommandHandler('Button6', Button6))

print("Telegram Starting...")
try:    
   updater.start_polling()
   updater.idle()
  
except:
   print("Error: unable to start thread")

while 1:
   pass

    
