#Selenium modules
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions

#python modules
import time

#user modules
import config


def automation(mobile=False):
    # Instantiate the webdriver with the executable location of MS Edge web driver 
    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument(config.edge["userDataPath"])
    if(mobile == True): #add an option to use a mobile user agent
        options.add_argument(config.edge["mobileUserAgent"])


    browser = Edge(executable_path=config.edge["driverPath"], options=options)

    # Simply just open a new Edge browser and go to bing.com
    browser.get('https://www.bing.com')

    time.sleep(1) #sleep for 1 sec

    search_term_file = open('search_terms.txt', 'r')
    search_terms = search_term_file.readlines()

    for term in search_terms:
        print("{0}".format(term))
        elem = browser.find_element_by_id('sb_form_q')
        elem.clear()
        time.sleep(0.25) #sleep for 250 milliseconds
        elem.send_keys(term + Keys.RETURN)
        time.sleep(0.25) #sleep for 250 milliseconds
        

    browser.close()

if __name__ == "__main__":
    automation()
    automation(mobile=True)