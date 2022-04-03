from bs4 import BeautifulSoup
import requests

#encapsulation is bad
#dictionnary in python
nickel_coins = {'25c': 5.05, '5c': 5.54, '10c': 2.07}

def return_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_market_info(soup):
    info = soup.find("span", class_ = "price-section__current-value").text
    return info

def get_cad_price_in_gram():
    nickel_url = 'https://markets.businessinsider.com/commodities/nickel-price?op=1'
    usd_cad_url = 'https://markets.businessinsider.com/currencies/usd-cad'
    price =  get_market_info(return_soup(nickel_url))
    usd_cad =  get_market_info(return_soup(usd_cad_url))
    price_in_cad = float(price)*float(usd_cad)
    cad_price_in_grams = price_in_cad/1000000
    return cad_price_in_grams

def get_coin_price(string):
    cad_price_in_grams = get_cad_price_in_gram()
    price_of_the_coin = cad_price_in_grams*nickel_coins[str(string)]
    return price_of_the_coin

def print_coin_price(string):
    price_of_the_coin = get_coin_price(string)
    print(price_of_the_coin)