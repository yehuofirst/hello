#-*- coding: utf-8 -*-
import json
import sys
import signal
from websocket import create_connection


def exit(signum, frame):
    print('You choose to stop me.')
    sys.exit()


signal.signal(signal.SIGINT, exit)
signal.signal(signal.SIGTERM, exit)


ws = create_connection("ws://127.0.0.1:55666/ws")
sub = '{"msgCode":"0","channel":["topsub_push"], "eventCode":"001","startMsgId":0}'
print 'send %s' % (sub)
ws.send_binary(sub)
i = 1
is_run = True

while is_run:
    try:
        result = ws.recv()
        if result == 'ping':
            print 'ping'
            ws.send_binary('pong')
        else:
            data_dict = json.loads(result)
            if 'msgId' in data_dict:
                print 'msgId:', data_dict['msgId']
                print data_dict
    except Exception:
        pass    
str = 'LM9j1ysfbF6JoAtme6W9jXa3X1HmGPnaxq'
print str.lower()