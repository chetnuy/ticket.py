#!/bin/python

import certifi
import urllib3
import  json
from colorama import  Fore
import argparse

#args parse
parser = argparse.ArgumentParser(description='Печать тикетов')
parser.add_argument('name',   type=str, nargs='+',
                    help='set ticket')
parser.add_argument('--graph', type=str, nargs='+',
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
def request(ticket):

    link = "https://query1.finance.yahoo.com/v7/finance/quote?lang=en-US&region=US&corsDomain=finance.yahoo.com&fields="
    fields = "symbol,marketState,regularMarketPrice,regularMarketChange,regularMarketChangePercent,preMarketPrice,preMarketChange,\
preMarketChangePercent,postMarketPrice,postMarketChange,postMarketChangePercent"

    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
    socket = http.request('GET', link+fields+'&symbols='+ticket)
    reply = json.loads(socket.data.decode('utf-8'))
    return reply


def format(reply):
    field = reply['quoteResponse']['result'][0]
    #print(field)
    #print(field.get('regularMarketChangePercent'))
    if field.get('regularMarketChangePercent') < 0:
        print(Fore.RED,end='')
    elif field.get('regularMarketChangePercent') > 0:
        print(Fore.GREEN,end='')


  #print(field.get('symbol'),field.get('regularMarketPreviousClose'),field.get('regularMarketPrice'),field.get('regularMarketChangePercent'))
    print('{:15} {:<10} {:<10}  {:5.2}'  .format(field.get('symbol'),field.get('regularMarketPreviousClose'),field.get('regularMarketPrice'),field.get('regularMarketChangePercent')))
    #print('{1}      {0}'.format('one', 'two'))

    print(Fore.RESET,end='')


for tick in args.name:
    ticket =request(tick)
    format(ticket)




# ticket =request('BTC-USD')
# #print(ticket)
# # print(ticket['quoteResponse']['result'][0]['symbol'],ticket['quoteResponse']['result'][0]['regularMarketPreviousClose'],ticket['quoteResponse']['result'][0]['regularMarketPrice'],ticket['quoteResponse']['result'][0]['regularMarketChangePercent'])
# # print(ticket['quoteResponse']['result'][0])
# format(ticket)
# ticket = request("AAPL")
# format(ticket)
# ticket = request("1810.HK")
# format(ticket)
# ticket = request("SBER.ME")
# format(ticket)
# ticket =request('AAPL')
# format(ticket)
# print(ticket['quoteResponse']['result'][0]['symbol'],ticket['quoteResponse']['result'][0]['regularMarketPrice'],ticket['quoteResponse']['result'][0]['preMarketChangePercent'])
