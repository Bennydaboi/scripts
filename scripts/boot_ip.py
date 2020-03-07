#coder :- Salman Faris

import sys
import time
import datetime
import telepot
import socket
import fcntl
import struct

bot = telepot.Bot('361308020:AAEbxl4L0AWZs4sYhvmzOP9Lw9SuCUvz960')
chat_id = 340690686
time.sleep(2)

def get_ip_address(ifname):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(
		s.fileno(),
		0x8915, # SIOCGIFADDR
		struct.pack('256s', ifname[:15])
	)[20:24])


#def handle(msg):
#    chat_id = msg['chat']['id']
#    command = msg['text']
#
#    print 'Got command: %s' % command
#
#    if command == 'ping':
#	bot.sendMessage(chat_id, 'System Responsive.')
#    elif command =='ip':
#	message = get_ip_address('wlan0')
#	bot.sendMessage(chat_id, message)
#	bot.sendMessage(chat_id, chat_id)

message = "IP address is\nelan0: %s." % get_ip_address('wlan0')
bot.sendMessage(chat_id, message)

#bot.message_loop(handle)
#print 'I am listening...'

#while 1:
#     time.sleep(10)
