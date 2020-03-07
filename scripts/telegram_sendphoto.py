#coder :- Salman Faris

import sys
import time
import random
import datetime
import telepot
import subprocess
import os

bot = telepot.Bot('361308020:AAEbxl4L0AWZs4sYhvmzOP9Lw9SuCUvz960')
chat_id_static = 340690686

#bot.sendMessage(chat_id_static, 'boop')
bot.sendPhoto(chat_id_static,photo=open('/home/pi/scripts/local.jpg','rb'))
