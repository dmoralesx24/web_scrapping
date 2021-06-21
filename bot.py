#TODO lIST FOR THIS BOT
# sign into site with the product 
# Find product for retail price of PS5 or Xbox Series X ($500)
# If product isn't available, wait until it is.
# Add product to the cart 
# Add payment
# Then checkout cart

##change steps to fit specific website checkout routine 

##POSSIBLE WEBSITES TO USE FOR PS5
##////////////////////////
#Walmart: PS5 | PS5 Digital Edition (last restock June 17)
#GameStop: PS5 | PS5 Digital Edition (last restock June 18)
#Target: PS5 | PS5 Digital Edition (last restock June 16)
#Sony: PS5 | PS5 Digital Edition (last restock June 17)
##////////////////////////

##POSSIBLE WEBSITES TO USE FOR Xbox Series X
##////////////////////////
#Walmart: PS5 | PS5 Digital Edition (last restock June 17)
#GameStop: PS5 | PS5 Digital Edition (last restock June 18)
#Target: PS5 | PS5 Digital Edition (last restock June 16)
#Microsoft: Xbox Series X | Xbox Series S (last restock June 8)
##////////////////////////


from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint, randrange
import time

# website_url = "https://www.amazon.com/gp/product/B0787DSQY6/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1"
website_url = "https://www.amazon.com/gp/product/B08FC5L3RG?tag=georiot-us-default-20&ascsubtag=grd-us-1031267595462810100-20&geniuslink=true"

test_url = ""
waitTime = 7
priceLimit = 500

class DavidShop:

    def __init__ (self, username, password):
        self.username = username
        self.password = password
        self.options = Options()
        self.binary = r'../../Program Files/Mozilla Firefox/firefox.exe'
        self.options.set_preference("browser.download.folderList",2)
        self.options.set_preference("browser.download.manager.showWhenStarting", False)
        self.options.set_preference("browser.download.dir","/Data")
        self.options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/vnd.ms-excel")
        self.options.binary = self.binary
        self.options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.driver = webdriver.Firefox(executable_path=r'./geckodriver.exe', options=self.options)

    def signIn(self):
        driver = self.driver

        ##enter username
        username_elem = driver.find_element_by_xpath("//input[@name='email']")
        username_elem.clear()
        #possibly fake typing here
        username_elem.send_keys(self.username)

        time.sleep(randint(int(waitTime/2), waitTime))

        username_elem.send_key(Keys.RETURN)

        time.sleep(randint(int(waitTime/2), waitTime))

        ## enter password
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        #possibly fake typing here
        password_elem.send_keys(self.password)

        time.sleep(randint(int(waitTime/2), waitTime))

        password_elem.send_key(Keys.RETURN)

    def findProduct(self):
        driver = self.driver
        driver.get(website_url)
        #time.sleep(randint(int(waitTime/2), waitTime))

        isAvailable = self.isProductAvailable()
        if isAvailable == 'Currently unavailable':
            time.sleep(randint(int(waitTime/2), waitTime))
            self.findProduct()
            
        elif isAvailable <= priceLimit:
            buy_now = driver.find_elemnt_by_name("but button")
            buy_now.click()
            time.sleep(randint(int(waitTime/2), waitTime))
            self.signIn()

            place_order = driver.find_element_by_name('place your order html tags')
            time.sleep(randint(int(waitTime/2), waitTime))
            place_order.click()
            time.sleep(randint(int(waitTime/2), waitTime))
        else:
            time.sleep(randint(int(waitTime/2), waitTime))
            self.findProduct()

    def isProductAvailable(self):
        driver = self.driver
        try:
            btn = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.ID, "buy-now-button"))
                #submit.buy-now
                #buy-now-button
            )
        except:
            print('There has been an error thrown...couldnt find element')
            btn = 'Currently Unavailable'
        
        return btn
        

    def closeBrowser(self):
        self.driver.close()

if __name__ == "__main__":
    shopBot = DavidShop("username", "password")
    shopBot.findProduct()
    shopBot.closeBrowser()




