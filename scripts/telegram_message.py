#coder :- Salman Faris

import sys
import time
import random
import datetime
import telepot
import subprocess
import os

bot = telepot.Bot('361308020:AAEbxl4L0AWZs4sYhvmzOP9Lw9SuCUvz960')
chat_id_static = '340690686'

message = str(sys.argv[1])

bot.sendMessage(chat_id_static, message)
