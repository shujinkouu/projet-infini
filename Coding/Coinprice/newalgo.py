from bs4 import BeautifulSoup
import requests


"""
copper = https://markets.businessinsider.com/commodities/copper-price
tin = https://markets.businessinsider.com/commodities/tin-price
zinc = https://markets.businessinsider.com/commodities/zinc-price
silver = https://markets.businessinsider.com/commodities/silver-price
nickel = https://markets.businessinsider.com/commodities/nickel-price
usd-cad = https://markets.businessinsider.com/currencies/usd-cad

"""

info_list = [('copper','https://markets.businessinsider.com/commodities/copper-price','ton'),('tin','https://markets.businessinsider.com/commodities/tin-price','ton'),('zinc','https://markets.businessinsider.com/commodities/zinc-price','ton'),('silver','https://markets.businessinsider.com/commodities/silver-price','toz'),('nickel','https://markets.businessinsider.com/commodities/nickel-price','ton'),('usd-cad','https://markets.businessinsider.com/currencies/usd-cad','None')]
prices_list = []


ton = 1000000
toz = 31.1035


try:
    for n in info_list:
        r = requests.get(n[1])
        soup = BeautifulSoup(r.text, 'html.parser')
        info = soup.find("span", class_ = "price-section__current-value").text
        if n[2] == 'ton':
            info = float(info)/ton
        elif n[2] == 'toz':
            info = float(info)/toz
        prices_list.append((n[0],info))
        #print(prices_list[n])
        #print("price is "+str(info))
        #print(n)
except:
    print('probably no internet')

print(prices_list)

import os
#This creates the database folder
cwd = os.getcwd()
path = os.getcwd() + "\\database"
try:
    os.mkdir(path)
except:
    pass
    
try:
    d =  open(cwd+ "\Database\\" + "metals.txt", "r+")
except:
    d =  open(cwd+ "\Database\\" + "metals.txt", "x")
    d.close()
    d = open(cwd+"\Database\\"+"metals.txt", "r+")
d = list(d)
#if d is an empty list it means this is the first use of the app the user is then prompted to log his password which is gonna be used to encrypt his credentials if not it asks the user for his password and then generated the key from his typed password
if d == []:
    cwd = os.getcwd()
    d = open(cwd + "\Database\\" + "metals.txt", 'a')
    d.write(str(prices_list))
    d.close()
else:
    d = open(cwd + "\Database\\" + "metals.txt", 'r')
    #print(str(d.text))
    the_list = d.read()
    d.close()
    print(the_list)

try:
    if str(prices_list) != str(the_list) and prices_list != []:
        print(prices_list)
        print(the_list)
        print("the price are outdated we need to delete metals.txt and remake it with today's info")
        os.remove(cwd+'\\database\\metals.txt')
        cwd = os.getcwd()
        d = open(cwd + "\Database\\" + "metals.txt", 'a')
        d.write(str(prices_list))
        d.close()
        print('and thus was done')
except:
    print('first excution nothing to see here')    
    







