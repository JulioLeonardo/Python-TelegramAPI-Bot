import telepot
from Chatbot import Chatbot

telegram = telepot.Bot("SEU TOKEN AQUI")
bot = Chatbot("CarrefourJBot")


def receiving_msg(msg):
    sentence = bot.listen(sentence=msg['text'])
    resp = bot.think(sentence)
    bot.speak(resp)
    content_type, chat_type, chat_id = telepot.glance(msg)
    telegram.sendMessage(chat_id, resp)


telegram.message_loop(receiving_msg)

while True:
    pass
