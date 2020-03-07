#coder :- Salman Faris

import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == 'ping':
	bot.sendMessage(chat_id, 'System Responsive.')
    elif command =='on':
	bot.sendMessage(chat_id, 'LED ON')
	GPIO.output(18, GPIO.HIGH)
    elif command == 'off':
	bot.sendMessage(chat_id, 'LED OFF')
	GPIO.output(18, GPIO.LOW)

bot = telepot.Bot('361308020:AAEbxl4L0AWZs4sYhvmzOP9Lw9SuCUvz960')
chat_id = 340690686
print 'I am listening...'

while 1:
	time.sleep(0.01)
	if GPIO.input(18)==1:
		print("Sound Heard")
		bot.sendMessage(chat_id, 'FUCK')
		time.sleep(2)
