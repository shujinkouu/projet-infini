from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

def get_perf_log_on_load(self, url, headless = True, filter = None):

    # init Chrome driver (Selenium)
    options = Options()
    options.headless = headless
    cap = DesiredCapabilities.CHROME
    cap['loggingPrefs'] = {'performance': 'ALL'}
    driver = webdriver.Chrome(desired_capabilities = cap, options = options)

    # record and parse performance log
    driver.get("https://www.blazetv.com/watch/channel/series/series/woaYbyV0BJww-good-morning-mug-club/episode/43-guvf0joujros-chris-cuomo-metoos-himself-on-leaked-phone-call-ep-38")
    if filter: log = [item for item in driver.get_log('performance')
                      if filter in str(item)]
    else: log = driver.get_log('performance')
    driver.close()

    print(log)
    
    