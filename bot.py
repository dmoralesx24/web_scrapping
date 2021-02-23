#TODO lIST FOR THIS BOT
# sign into site with the product 
# Find product for retail price of PS5 or Xbox Series X ($500)
# If product isn't available, wait until it is.
# Add product to the cart 
# Add payment
# Then checkout cart

##change steps to fit specific website checkout routine 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException
from random import randict, randrange
import time
import random 

website_url = "get url you're gonna use David"
test_url = ""
waitTime = 7
priceLimit = 500

hello = "Hello World"
print (hello) 

class DavidShop:

    def __init__ (self, username, password):
        self.username = username
        self.password = password
        
        self.driver = webdriver.Firefox()


    def signIn(self):
        driver = self.driver

        ##enter username
        username_elem = driver.find_element_by_xpath("//input[@name='email']")
        username_elem.clear()
        #possibly fake typing here
        username_elem.send_keys(self.username)

        time.sleep(randict(int(waitTime/2), waitTime))

        username_elem.send_key(Keys.RETURN)

        time.sleep(randict(int(waitTime/2), waitTime))

        ## enter password
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        #possibly fake typing here
        password_elem.send_keys(self.password)

        time.sleep(randict(int(waitTime/2), waitTime))

        password_elem.send_key(Keys.RETURN)

    def findProduct(self):
        driver = self.driver
        driver.get(website_url)
        time.sleep(randict(int(waitTime/2), waitTime))

        isAvailable = self.isProductAvailable()
        if isAvailable == 'Currently unavailable':
            time.sleep(randict(int(waitTime/2), waitTime))
            self.findProduct()
        elif isAvailable <= priceLimit:
            buy_now = driver.find_elemnt_by_name("but button")
            buy_now.click()
            time.sleep(randict(int(waitTime/2), waitTime))
            self.signIn()

            place_order = driver.find_element_by_name('place your order html tags')
            time.sleep(randict(int(waitTime/2), waitTime))
            place_order.click()
            time.sleep(randict(int(waitTime/2), waitTime))
        else:
            time.sleep(randict(int(waitTime/2), waitTime))
            self.findProduct()

    def isProductAvailable(self):
        driver = self.driver
        available = driver.find_element_by_class_name("find availabilty by class name")
        if available == 'Currently Unavailable':
            print(f'AVAILABLE: {available}')
            return available
        else:
            print(f'PRICE: {available}')
            return float(available[1:])

    def closeBrowser(self):
        self.driver.close()

if __name__ == "__main__":
    shopBot = DavidShop("username", "password")
    shopBot.findProduct()
    shopBot.closeBrowser()




