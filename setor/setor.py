#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import random
import socks
import socket
import urllib2
import httplib
import logging
import inspect
from logging import handlers

import userAgents

# Path to save the logs.
# If not exists, doing to create.
log_path = '/var/logs/setor'
if not os.path.exists(log_path):
    os.makedirs(log_path)

## Terminal Colors
RED = '\033[91m'
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
END_COLOR = '\033[0m'

URL_TO_CHECK_PUBLIC_IP = [
    'https://api.ipify.org',
    'http://ip.42.pl/raw',
    'http://myip.dnsomatic.com',
    'http://checkip.amazonaws.com'
]

# Chcecking privillage
if os.getuid() != 0:
    print "\n{}[-] Please Access as root..!{}\n".format(RED, END_COLOR)
    sys.exit()
else: pass


def Banner():
    print("\033c")
    print """
           d888888o.   8 8888888888 8888888 8888888888 ,o888888o.     8 888888888o.
         .`8888:' `88. 8 8888             8 8888    . 8888     `88.   8 8888    `88.
         8.`8888.   Y8 8 8888             8 8888   ,8 8888       `8b  8 8888     `88
         `8.`8888.     8 8888             8 8888   88 8888        `8b 8 8888     ,88
          `8.`8888.    8 888888888888     8 8888   88 8888         88 8 8888.   ,88'
           `8.`8888.   8 8888             8 8888   88 8888         88 8 888888888P'
            `8.`8888.  8 8888             8 8888   88 8888        ,8P 8 8888`8b
        8b   `8.`8888. 8 8888             8 8888   `8 8888       ,8P  8 8888 `8b.
        `8b.  ;8.`8888 8 8888             8 8888    ` 8888     ,88'   8 8888   `8b.
         `Y8888P ,88P' 8 888888888888     8 8888       `8888888P'     8 8888     `88.

        {}SETOR (SEO TOR) - Bot TOR to visit the webpages with unique IP's and random times.{}
        {}CREDIT ^$^ Summon Agus - IBTeam{}
        {}LICENSE - MIT{}
    """.format(YELLOW, END_COLOR, RED, END_COLOR, RED, END_COLOR)


def functionLogger(file_level, console_level=None):
    ''' `functionLogger` to save the log's file every midnight/days. '''
    function_name = inspect.stack()[1][3]
    logger = logging.getLogger(function_name)
    logger.setLevel(logging.DEBUG)

    if console_level != None:
        ch = logging.StreamHandler()
        ch.setLevel(console_level)
        ch_format = logging.Formatter('%(asctime)s - %(message)s')
        ch.setFormatter(ch_format)
        logger.addHandler(ch)

    file_log = os.path.join(log_path, "SETOR-log")
    fh = logging.handlers.TimedRotatingFileHandler(file_log, when='midnight', utc=False)
    fh.suffix = "_%Y-%m-%d" + ".log"
    fh.setLevel(file_level)
    fh_format = logging.Formatter('%(asctime)s - %(message)s')
    fh.setFormatter(fh_format)
    logger.addHandler(fh)
    return logger


log_logger = functionLogger(logging.DEBUG, logging.ERROR)


def visitLink(link, log_choice, host_conf, port_conf):
    Banner()
    try:
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, host_conf, port_conf, True)
        socket.socket = socks.socksocket
        time.sleep(0.5)
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', random.choice(userAgents.userAgents))]

        print "{}[i]{} Checking your public IP...".format(CYAN, END_COLOR)
        checking_ip = opener.open(random.choice(URL_TO_CHECK_PUBLIC_IP)).read().replace('\n', '')
        print "{}[i]{} IP now   - {}".format(CYAN, END_COLOR, checking_ip) #Checking new IP
        time.sleep(0.5)

        print "{}[i]{} Visit to - {}".format(CYAN, END_COLOR, link)
        opener.open(link)                                                  #Opening the link
        print "{}[i] Success visited!{}".format(GREEN, END_COLOR)

        if log_choice == True:
            log_logger.info("IP: {} - Succes visited to: {}".format(checking_ip, link))

    except urllib2.HTTPError as e:
        print "{}[i] {} - {}{}".format(YELLOW, e, link, END_COLOR)
        if log_choice == True:
            log_logger.info("{} - {}".format(e, link))

    except urllib2.URLError as e:
        print "{}[i] {} - {}{}".format(YELLOW, e, link, END_COLOR)
        if log_choice == True:
            log_logger.info("{} - {}".format(e, link))

    except httplib.HTTPException as e:
        print "{}[i] {} - {}{}".format(YELLOW, e, link, END_COLOR)
        if log_choice == True:
            log_logger.info("{} - {}".format(e, link))

    except socks.SOCKS4Error as e:
        print "{}[i] {} - {}{}".format(YELLOW, e, link, END_COLOR)
        if log_choice == True:
            log_logger.info("{} - {}".format(e, link))
    
    print "{}[i]{} Restating TOR to get new IP...".format(CYAN, END_COLOR)
    time.sleep(0.5)

    #Restarting the TOR to get new IP, this bassed for Ubuntu. other linux use different method.
    os.system("sudo service tor restart")

    #Random for time wait, just optionally.
    wait_time = random.randint(10, 15)
    print "{}[i]{} Wait for {} seconds...".format(CYAN, END_COLOR, wait_time)

    #Waiting with random between 10 -> 15 seconds from `wait_time`.
    time.sleep(wait_time)


def main():
    Banner()
    print """{} // OPTIONS:{}\n A. Single Link\n B. Multiple Links\n""".format(GREEN, END_COLOR)
    choice = raw_input("{}[+]{} Type your choice [a/B]: ".format(GREEN, END_COLOR))

    host_input = raw_input("{}[+]{} Host TOR (Enter to set default: 127.0.0.1): ".format(GREEN, END_COLOR))
    port_input = raw_input("{}[+]{} Port TOR (Enter to set default: 9050): ".format(GREEN, END_COLOR))

    host_conf = '127.0.0.1'
    port_conf = 9050

    if host_input != '':
        host_conf = host_input
    if port_input != '':
        port_conf = int(port_input)

    if choice.lower() == 'a':
        inp_single_link = raw_input("{}[+]{} Paste your single link: ".format(GREEN, END_COLOR))

        log_choice = raw_input("{}[+]{} Are you need to save as log? [y/N]: ".format(GREEN, END_COLOR))
        if log_choice.lower() == 'y': log_choice = True
        else: log_choice = False

        try:
            while True:
                visitLink(inp_single_link, log_choice, host_conf, port_conf)
        except KeyboardInterrupt:
            print "{}[-] Finished!{}".format(YELLOW, END_COLOR)
            sys.exit()

    elif choice.lower() == 'b':
        inp_file_links = raw_input("{}[+]{} Type your file links *.txt: ".format(GREEN, END_COLOR))
        urls = [ line.strip() for line in open(inp_file_links, 'r') if line.strip() != '' ]

        log_choice = raw_input("{}[+]{} Are you need to save as log? [y/N]: ".format(GREEN, END_COLOR))
        if log_choice.lower() == 'y': log_choice = True
        else: log_choice = False

        try:
            while True:
                for link in urls:
                    visitLink(link, log_choice, host_conf, port_conf)
        except KeyboardInterrupt:
            print "{}[-] Finished!{}".format(YELLOW, END_COLOR)
            sys.exit()

    else: print "{}[!] Wrong input!{}".format(RED, END_COLOR)
    logging.shutdown()

if __name__ == '__main__':
    main()
