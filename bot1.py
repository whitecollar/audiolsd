import telebot
import time

TOKEN = '1829642580:AAEojR4JRS4X4oZr0qRz_q8ppO8naSLokKA'



def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        chatid = m.chat.id
        if m.content_type == 'text':
            text = m.text
            tb.send_message(chatid, text)


tb = telebot.TeleBot(TOKEN)
audio = open('./pqlik.wav', 'rb')
tb.send_audio('-1001206972540', audio)
#file_id = './test.wav'
#tb.send_audio('audiolsd123', file_id)


#tb.set_update_listener(listener) #register listener
#tb.polling()
#Use none_stop flag let polling will not stop when get new message occur error.
#tb.polling(none_stop=True)
# Interval setup. Sleep 3 secs between request new message.
#tb.polling(interval=3)
#
