from bs4 import BeautifulSoup
import requests

#New dictionnaries
#That's canadian coin
#1cent (Metal Composition%, Metal Composition%, Metal Composition%)-Weight-Diameter-Thickness-
#one_cent = {'1920-1941': '(95.5%copper, 3%tin, 1.5%zinc)-3.24g','1942-1977': '(98%copper, 0.5%tin, 1.5%zinc)-3.24g','1978-1979': '(98%copper, 1.75%tin, 0.25%zinc)-3.24g','1980-1981':'(98%copper, 1.75%tin, 0.25%zinc)-2.8g','1982-1996':'(98% copper, 1.75% tin, 0.25% zinc)-2.5g','1997-1999':'(98.4%zinc, 1.6%copper)-2.25g','2000-2012_mag':'(94%steel, 1.5%nickel, 4.5%copper)-2.35g','2000-2012_nmag':'(98.4%zinc, 1.6%copper)-2.35g'}
#5cent
# = {'1920-1921':,'1922-1942':,'1942-1943':,'1944-1945':,'1946-1951':,'1951-1954':,'1955-1981':,'1982-2001+2006(nologo)':,'2000-p':,}
#10cent
# = {'1958-1919':,'1920-1967':,'1967-1968':,'1968-1977':,'1978':,'1979-2000':,'2000-p':,}
#25cent
# = {'1920-1952':,'1953-1967':,'1967-1968':,'1968-1977':,'1978-2001':,'2000-p':,}
#loonie
# = {'1935-1967':,'1968-1982':,'1982-1986':,'1987':,'1988-2002':,'2003-2012':,'2012-p':,}
#toonie
# = {'1996-2012':,'2012-p':,}

#dictionnary in python
#the nickel dollar (pre-2012)
nickel_coins = {'25c': 5.05, '5c': 4.56, '10c': 2.07}
silver_coins = {'25c':,'5c':,'10c':,'1$':}

#Metal spt price that needs to be known
#tin, copper, zinc, steel, silver, nickel, bronze
#Calculate metal spotprice first save it in database in grams followed with the date
#For each coin mutiply % of metal with weight to get weight of the metal per coin, then multiply those with the spotprice per gram to get the worth in each metal. Add them to get the worth of the coin.
#For example 1920-1941 1cent -> (95.5%copper, 3%tin, 1.5%zinc)-3.24g -> price of the coin = (0.955 * copperspot * 3.24g) + (0.03 * tinspot * 3.24g) + (0.015 * zincspot * 3.24g)

#there's the 75% copper, 25% nickel 5cent coin
#there's the 50% silver 10 cent coin
#The pre 2012 toonie
#there's maybe another coin that is from parts
parts_coins = {'75/25-5c': 1,'50/50'}

#Regular worthless coins
worthless_coins = {}

url_list = {'silver_toz': 'https://markets.businessinsider.com/commodities/silver-price', 'gold_toz': '', 'nickel_':}




>>> t = {'nickel':64,'gold':2000,'silver':30}
>>> t
{'nickel': 64, 'gold': 2000, 'silver': 30}
>>> t[nickel]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'nickel' is not defined
>>> t['nickel']
64
>>> t['nickel'] = 5
>>> t
{'nickel': 5, 'gold': 2000, 'silver': 30}
>>>

#trys to open it if it doesn't open simply creates one and then opens it
try:
    d =  open(cwd+ "\Database\\" + "credentials.txt", "r+")
except:
    d =  open(cwd+ "\Database\\" + "credentials.txt", "x")
    d.close()
    d = open(cwd+"\Database\\"+"credentials.txt", "r+")


####New space to deal with database and saving the spot/date
def databaseinit():
    os.getcwd()
    path = os.getcwd() + "\\database"
    try:
        os.mkdir(path)
    except:
        pass
        #print("we already have a database")

def saveindt(a, service_name):
    cwd = os.getcwd()
    d = open(cwd + "\Database\\" + "credentials.txt", 'a') 
    d.write('\n'+service_name+a)
    d.close()


####

#>>> a = {'1920-1941': '(95.5%copper, 3%tin, 1.5%zinc)-3.24g'}
#>>> a['1920-1941']
#'(95.5%copper, 3%tin, 1.5%zinc)-3.24g'

#Dictionnary of weight and measure could be something great!
#metals = coin[coin.find('(')+1:coin.find(')')]
#weight = coin[coin.find('-')+1:coin.find('g')]
#Metals compute
#list_of_metals = metals.split(',')
#for n in list_of_metals:
#    metal = n[n.find('%')+1:]
#    print('metal is: '+metal)
#    percentage = n[:n.find('%')]
#    if percentage[0] == ' ':
#        percentage = percentage[1:]
#    print('percentage is: '+percentage)


def sel_coin():
    coin = input('what\'s the coin?')
    year = input('what\s the year?')
    year = int(year)
    if coin == '1cent':
        print('hi')
        print(year)
        if year >= 1920 and year <= 1941:
            print('hi')
            timeframe = '1920-1941'
        if year >= 1942 and year <= 1977:
            timeframe = '1942-1977'
        if year >= 1978 and year <= 1979:
            timeframe = '1978-1979'
        if year >= 1980 and year <= 1981:
            timeframe = '1980-1981'
        if year >= 1982 and year <= 1996:
            timeframe = '1982-1996'
        if year >= 1997 and year <= 1999:
            timeframe = '1997-1999'
        if year >= 2000 and year <= 2012:
            mag = input('magnetic? [y/n]') 
            if mag.find('y') != -1:
                timeframe = '2000-2012_mag'
            if mag.find('n') != -1:
                timeframe = '2000-2012_nmag'
        coin = one_cent[timeframe]
        return coin
    
    
    if coin = '5cent':
        if year >= 1920 and year <= 1921:
            timeframe = '1920-1921'
        if year <= 1922 and year >= 1942:
            timeframe = '1922-1942'
        if year <= 1942 and year >= 1943:
            timeframe = '1942-1943'
        if year <= 1944 and year >= 1945:
            timeframe = '1944-1945'
        if year <= 1946 and year >= 1951:
            timeframe = '1946-1951'
        if year <= 1951 and year >= 1954:
            timeframe = '1951-1954'
        if year <= 1955 and year >= 1981:
            timeframe = '1955-1981'
        if year <= 1982 and year >= 2001 :
            timeframe = '1982-2001'
        if year <= 2000 and year >= 2022 :
            if year = 2006:
                print()
            timeframe = '2000-2022'
        coin = five_cent[timeframe]
        return coin


#Too many function this can be streamlined in an easier faschion

def return_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_market_info(soup):
    info = soup.find("span", class_ = "price-section__current-value").text
    return info

def get_spot(url):
    soup = return_soup(url)
    spot = get_market_info(soup)
    return spot

def get_cad_price_in_gram():
    nickel_url = 'https://markets.businessinsider.com/commodities/nickel-price?op=1'
    usd_cad_url = 'https://markets.businessinsider.com/currencies/usd-cad'
    price =  get_market_info(return_soup(nickel_url))
    usd_cad =  get_market_info(return_soup(usd_cad_url))
    price_in_cad = float(price)*float(usd_cad)
    cad_price_in_grams = price_in_cad/1000000
    return cad_price_in_grams

def get_nickel_coin_price(string):
    cad_price_in_grams = get_cad_price_in_gram()
    price_of_the_coin = cad_price_in_grams*nickel_coins[str(string)]
    return price_of_the_coin
    
def print_coin_price(string):
    price_of_the_nickel_coin = get_nickel_coin_price(string)
    print(price_of_the_nickel_coin)