#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#author by Dullah ID
#recode By Zacky Tricker
#https://github.com/ZAKI-ZK

import requests, re
logo = """
\033[1;92m .o88b.  .d88b.  d8b   db db    db d88888b d8888b. d888888b 
d8P  Y8 .8P  Y8. 888o  88 88    88 88'     88  `8D `~~88~~' 
8P      88    88 88V8o 88 Y8    8P 88ooooo 88oobY'    88    
8b      88    88 88 V8o88 `8b  d8' 88~~~~~ 88`8b      88    
Y8b  d8 `8b  d8' 88  V888  `8bd8'  88.     88 `88.    88    
 `Y88P'  `Y88P'  VP   V8P    YP    Y88888P 88   YD    YP    
                  """                                          
                                                     
print (logo)
print('Convert Cookie To token')
cookie = input('Input Cookie >>> \033[1;96m')
try:
    data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
        'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # don't change this user agent.
        'referer'                   : 'https://m.facebook.com/',
        'host'                      : 'm.facebook.com',
        'origin'                    : 'https://m.facebook.com',
        'upgrade-insecure-requests' : '1',
        'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control'             : 'max-age=0',
        'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'content-type'              : 'text/html; charset=utf-8'
    }, cookies = {
        'cookie'                    : cookie
    })
    find_token = re.search('(EAAA\w+)', data.text)
    results    = '\033[1;91m\n* Fail : maybe your cookie invalid !!' if (find_token is None) else '\033[1;92m\n* Your fb access token :\033[1;93m ' + find_token.group(1)
except requests.exceptions.ConnectionError:
    results    = '\033[1;91m\n* Fail : no connection here !!'
except:
    results    = '\033[1;91m\n* Fail : unknown errors, please try again !!'

print(results)
