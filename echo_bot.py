import telepot
import time

# For this bot install telepot module. Please visit: https://github.com/nickoala/telepot
# a simple bot that repeat all you send it.
def handle(msg):
    #Here I prepare chat id and message
    chat_id = msg['chat']['id']
    text = msg['text']
    
    #Now i send to the user the same thing
    bot.sendMessage(chat_id,text)

# Crate the bot
bot = telepot.Bot('*** Your token ***')
bot.notifyOnMessage(handle)
print 'I am listening ...'

while 1:
    time.sleep(10)
