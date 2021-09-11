import telepot
from telepot.loop import MessageLoop
import time
import os

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    #print("CHAT ID: ", chat_id)

    username = msg['from']['username']
    user_id = msg['from']['id']

    print("USERNAME: ", username)
    print("USER ID:", user_id)
    print("Message:", msg['text'])


    if content_type == 'text':
        text = msg['text']


    if username == '#YOUR TELEGRAM USERNAME':
        if text == "/Etherwake_MY_PC":
            try:
                bot.sendMessage(chat_id,"Trying to power on PC . . .")
                os.system("sudo etherwake #(YOUR EHTERNET NETWORK CARD MAC HERE)")
                bot.sendMessage(chat_id, "PC BOOTED SUCCESSFULLY")
            except:
                bot.sendMessage(chat_id, "PC IS OFFLINE, CAN'T BOOT")
        else:
            bot.sendMessage(chat_id, "Wrong command! RETRY.")


TOKEN = '#YOUR BOT TOKEN HERE'

bot = telepot.Bot(TOKEN)
MessageLoop(bot,handle).run_as_thread()
print('listening...')

while 1:
    time.sleep(10)