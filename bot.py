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
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint, randrange
import time
from dotenv import dotenv_values

#REGION PS5 links
amazon_url = 'https://www.amazon.com/Sony-Playstation-Disk/dp/B082S2LYV1/ref=sr_1_3?crid=NQFUKMT8FF9R&dchild=1&keywords=playstation+5+console&qid=1635369528&sprefix=plays%2Caps%2C136&sr=8-3'
walmart_url = 'https://www.walmart.com/ip/Sony-PlayStation-5-Video-Game-Console/165545420'
target_url = 'https://www.target.com/p/playstation-5-console/-/A-81114595?clkid=cf3af1bdN584011ebb49742010a246e3a&lnm=81938&afid=Future%20PLC.&ref=tgt_adv_xasd0002'
bestbuy_url = 'https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149'
bestbuy_test_url = 'https://www.bestbuy.com/site/asus-11-6-chromebook-intel-celeron-4gb-memory-32gb-emmc-flash-memory-gray-grey/6449513.p?skuId=6449513'
#END REGION

website_url = bestbuy_test_url
waitTime = 7
priceLimit = 500

class DavidShop:

    def __init__ (self, username, password):
        self.username = username
        self.password = password
        self.options = Options()
        
        self.options.add_argument("--window-size=1920x1080")
        self.options.add_argument("--verbose")

        # self.driver = webdriver.Firefox(executable_path=r'./geckodriver.exe', options=self.options)
        self.driver = webdriver.Chrome(options=self.options)


    def signIn(self):
        driver = self.driver
        ##enter username
        username_elem = driver.find_element_by_xpath("//input[@name='email']")

        username_elem.clear()
        #possibly fake typing here
        username_elem.send_keys(self.username)

        # time.sleep(randint(int(waitTime/1), waitTime))

        username_elem.send_keys(Keys.ENTER)

        time.sleep(randint(int(waitTime/1), waitTime))


        ## enter password
        # password_elem = self.webDriverWait(1, 'xpath', "//input[@name='password']")
        password_elem = driver.find_element_by_xpath("//input[@name='password']")

        password_elem.clear()
        #possibly fake typing here
        password_elem.send_keys(self.password)

        # time.sleep(randint(int(waitTime/1), waitTime))

        password_elem.send_keys(Keys.ENTER)

    def findProduct(self):
        driver = self.driver
        driver.get(website_url)
        time.sleep(randint(int(waitTime/1), waitTime))
        
        # NOTE: checks if buy button is available
        btn = self.isProductAvailable("add-to-cart-button")
        if btn == 'Currently Unavailable':
            # time.sleep(randint(int(waitTime/1), waitTime))
            self.findProduct()
         
        btn.click()
        time.sleep(randint(int(waitTime/1), waitTime))
        
        # NOTE: Looks for cart button    todo: figure out an exit strategy if it doesn't find the button
        btn2 = self.isProductAvailable("go-to-cart-button")
        btn2.click()
        # self.signIn()

        time.sleep(randint(int(waitTime/1), waitTime))

        place_order = driver.find_element_by_name('place your order html tags')
        place_order.click()
        time.sleep(randint(int(waitTime/1), waitTime))
        

    def isProductAvailable(self, tagname):
        driver = self.driver
        btn = None
        try:
            btn = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.CLASS_NAME, tagname))
            )
        except:
            btn = 'Currently Unavailable'
        
        return btn
        
    def webDriverWait(self, time, id, name):
        enumElement = {'id': By.ID, 'classname': By.CLASS_NAME, 'xpath': By.XPATH}
        driver = self.driver
        res = {'found': False}
        try:
            element = WebDriverWait(driver, time).until(
                EC.presence_of_element_located((enumElement[id], name)))
            res['found'] = True
            res['element'] = element
        except:
            print('There has been an error thrown...couldnt find element')
        
        return res

    def closeBrowser(self):
        self.driver.close()

if __name__ == "__main__":

    config = dotenv_values('.env')
    shopBot = DavidShop(config['AMAZON_USERNAME'], config['AMAZON_PASSWORD'])
    shopBot.findProduct()
    shopBot.closeBrowser()




