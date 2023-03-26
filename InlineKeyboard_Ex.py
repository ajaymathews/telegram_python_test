from telegram.ext import Updater,CommandHandler,MessageHandler,CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

import RPi.GPIO as gpio
from time import sleep
gpio.setmode(gpio.BOARD)
gpio.setup(3,gpio.OUT,initial=0)
gpio.setup(5,gpio.OUT,initial=0)
gpio.setup(7,gpio.OUT,initial=0)

"""
def led_on_off():
    global led
    if query.data=='on':
        print("LED ON")
        gpio.output(led_d[led],1)
    else:
        print("LED OFF")   
        gpio.output(led_d[led],0)
"""
led_d={'l1':3,'l2':5,'l3':7}



led=0
stat=0


def menu_1_key():
    keyb=[[InlineKeyboardButton('LED',callback_data='led')],
          [InlineKeyboardButton('Motor',callback_data='mot')],
          [InlineKeyboardButton('Sensors',callback_data='sens')],
          [InlineKeyboardButton('Home',callback_data='home')]]
    return InlineKeyboardMarkup(keyb)

def led_key():
    keyb=[[InlineKeyboardButton('LED 1',callback_data='l1')],
          [InlineKeyboardButton('LED 2',callback_data='l2')],
          [InlineKeyboardButton('LED 3',callback_data='l3')],
          [InlineKeyboardButton('Home',callback_data='home')]]
    return InlineKeyboardMarkup(keyb)

def led_cnt_key():
    keyb=[[InlineKeyboardButton('On',callback_data='on')],
          [InlineKeyboardButton('Off',callback_data='off')],
          [InlineKeyboardButton('Home',callback_data='home')]]
    return InlineKeyboardMarkup(keyb)
    

def led_resp():
    return "LED "+led[-1]+stat

def menu_1_resp():
    return "Click on Choice:"

def menu_act(bot,update):
    global led
    global stat
    query=update.callback_query
    print(query.data)
    if query.data=='led':
        print("If")
        #update.message.reply_text("LED Pressed")
        #bot.send_message(chat_id=query.message.chat_id,text='test')
        bot.edit_message_text(chat_id=query.message.chat_id,
                              message_id=query.message.message_id,
                              text=menu_1_resp(),
                              reply_markup=led_key())

    elif query.data=='l1' or query.data=='l2' or query.data=='l3':
        led=query.data
        bot.edit_message_text(chat_id=query.message.chat_id,
                              message_id=query.message.message_id,
                              text="LED "+led[-1]+" Menu\n"+menu_1_resp(),
                              reply_markup=led_cnt_key())
    
    elif query.data=='home':
        bot.edit_message_text(chat_id=query.message.chat_id,
                              message_id=query.message.message_id,
                              text=menu_1_resp(),
                              reply_markup=menu_1_key())
        
    elif query.data=='on' or query.data=='off':
        stat=query.data
        print("led ",led)
        print("stat ",stat)
        print("test1")
        #led_on_off()
        if stat=='on':
            print("LED ON")
            gpio.output(led_d[led],1)
        else:
            print("LED OFF")   
            gpio.output(led_d[led],0)
        print("test2")
        bot.edit_message_text(chat_id=query.message.chat_id,
                              message_id=query.message.message_id,
                              text="LED "+stat,
                              reply_markup=led_cnt_key())
        print("test3")
        

    else:
        print("else")
        update.message.reply_text("Somthing")

    print("out")
        


def start(bot,update):
    update.message.reply_text(menu_1_resp(),reply_markup=menu_1_key())
    print("Bot ready!")
    for i in [3,5,7]:
        gpio.output(i,1)
        sleep(1)

    for i in [3,5,7]:
        gpio.output(i,0)
        sleep(1)


updater=Updater(token='627333566:AAGanhIPY2BP7UqOJcdAhjYR1mOJZG6OuyM')
disp=updater.dispatcher

disp.add_handler(CommandHandler('start',start))
disp.add_handler(CallbackQueryHandler(menu_act))
#disp.add_handler(CallbackQueryHandler(test,pattern='led'))
updater.start_polling()

updater.idle()
