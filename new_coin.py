from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from spec import *
from dotenv import load_dotenv
import os
import time
from pyotp import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Setting:
# env = "https://testnet.btse.io"
env = "https://spot.oa.btse.io"

#Spot 2FA
totp = TOTP("BJNYV4C4ZXLK3HT6")
#testnet 2FA
# totp = TOTP("T6S7BGBZE6KJHJ36")


def Login(driver):

    driver.get(f"{env}/en/login")
    driver.find_element(By.XPATH,"//input[@class='input-inline-input']").send_keys('zxc5131210')
    driver.find_element(By.XPATH,"//div[@class='flex-box flex-column justify-center'][2]//input[@class='input-inline-input']").send_keys('Aa12345678')
    time.sleep(1)
    driver.find_element(By.XPATH,"//button[@class='w-100 btse-button inline-flex flex-row justify-center items-center border-box button-type--confirm button-size--bigger']").click()
    time.sleep(1)
    token = totp.now()
    driver.find_element(By.XPATH,("(//input[@class='input-inline-input'])[3]")).send_keys(token);
    time.sleep(2)


def ChangeCoin(driver):
    # icon/search
    driver.get(f"{env}/en/trading/BTC-USD")
    ele = driver.find_element(By.XPATH,"//div[@class='market-menu__button']")
    ActionChains(driver).move_to_element(ele).perform()
    driver.find_element(By.XPATH,"//input[@class='market-search-input']").send_keys(New_Coin)
    time.sleep(5)
    driver.find_element(By.XPATH,"//div[@class='market-name__text text-main']").click()

def USD(driver):
    
    # SupportedQuoteCoins 
    ele = driver.find_element(By.XPATH,"//header[@class='header no-select']")
    ActionChains(driver).move_to_element(ele).perform()
    driver.find_element(By.XPATH,"//div[@class='action-wrap']").click()
    time.sleep(5)
    print(minValidPrice)
    driver.find_element(By.XPATH,"(//span[text()=' USD '])[2]").click();
    ele = driver.find_element(By.XPATH,"//header[@class='header no-select']")
    ActionChains(driver).move_to_element(ele).perform()
    time.sleep(2)
    # limit buy
    min_price = driver.find_element(By.XPATH,"//input[@class='w-70 border-none tx-align--right input']")
    ActionChains(driver).double_click(min_price).perform()
    min_price.send_keys(Keys.DELETE)
    min_price.send_keys(minValidPrice)
    min_size = driver.find_element(By.XPATH,"//div[@class='__form_item']//input")
    ActionChains(driver).click(min_size).perform()
    min_size.send_keys(minOrderSize)
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # market buy
    driver.find_element(By.XPATH,"//li[@class='-item'][1]/span").click()
    driver.find_element(By.XPATH,"//input[@class='w-70 border-none tx-align--right input']").send_keys('10')
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # oco buy
    driver.find_element(By.XPATH,"//li[@class='-item'][2]/span").click()
    driver.find_element(By.XPATH,"//input[@id='spotOcoPriceInput']").send_keys(minValidPrice)
    driver.find_element(By.XPATH,"//input[@id='spotOcoStopPriceInput']").send_keys(big_price)
    driver.find_element(By.XPATH,"//input[@id='spotOcoSizeInput']").send_keys(minOrderSize)
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # index buy
    driver.find_element(By.XPATH,"//li[@class='-item'][3]/span").click()
    index_price = driver.find_element(By.XPATH,"//div[@class='input--container flex-box justify-between items-center'][1]//input")
    ActionChains(driver).double_click(index_price).perform()
    index_price.send_keys(Keys.DELETE)
    index_price.send_keys(minValidPrice)
    driver.find_element(By.XPATH,"//div[@class='input--container flex-box justify-between items-center'][2]//input").send_keys(minOrderSize)
    driver.find_element(By.XPATH,"//div[@class='input--container flex-box justify-between items-center'][3]//input").send_keys('10')
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # limit sell
    driver.find_element(By.XPATH,"//div[@class='spot-order-type-tab sell']").click()
    driver.find_element(By.XPATH,"//li[@class='-item'][1]/span").click()
    price = driver.find_element(By.XPATH,"//input[@class='w-70 border-none tx-align--right input']")
    ActionChains(driver).double_click(price).perform()
    price.send_keys(Keys.DELETE)
    price.send_keys(big_price)
    min_size = driver.find_element(By.XPATH,"//div[@class='__form_item']//input")
    ActionChains(driver).click(min_size).perform()
    min_size.send_keys(minOrderSize)
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # market sell
    driver.find_element(By.XPATH,"//li[@class='-item'][1]/span").click()
    driver.find_element(By.XPATH,"//input[@class='w-70 border-none tx-align--right input']").send_keys(minOrderSize)
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # oco sell
    driver.find_element(By.XPATH,"//li[@class='-item'][2]/span").click()
    driver.find_element(By.XPATH,"//input[@id='spotOcoPriceInput']").send_keys(big_price)
    driver.find_element(By.XPATH,"//input[@id='spotOcoStopPriceInput']").send_keys(minValidPrice)
    driver.find_element(By.XPATH,"//input[@id='spotOcoSizeInput']").send_keys(minOrderSize)
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # index sell
    driver.find_element(By.XPATH,"//li[@class='-item'][3]/span").click()
    index_price = driver.find_element(By.XPATH,"//div[@class='input--container flex-box justify-between items-center'][1]//input")
    ActionChains(driver).double_click(index_price).perform()
    index_price.send_keys(Keys.DELETE)
    index_price.send_keys(big_price)
    driver.find_element(By.XPATH,"//div[@class='input--container flex-box justify-between items-center'][2]//input").send_keys(minOrderSize)
    driver.find_element(By.XPATH,"//div[@class='input--container flex-box justify-between items-center'][3]//input").send_keys('10')
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    
def BTC(driver):
    try:
        # Change to BTC
        ele = driver.find_element(By.XPATH,"//header[@class='header no-select']")
        ActionChains(driver).move_to_element(ele).perform()
        driver.find_element(By.XPATH,"//div[@class='action-wrap']").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"(//span[text()=' BTC '])[2]").click();
        time.sleep(2)
        driver.find_element(By.XPATH,("//span[text()='LIMIT']")).click();
        driver.find_element(By.XPATH,("//input[contains(@class,'w-70 border-none')]")).clear();
        time.sleep(2)
    except:
        pass
    
    
def ETH(driver):
    try:
        # Change to ETH
        ele = driver.find_element(By.XPATH,"//header[@class='header no-select']")
        ActionChains(driver).move_to_element(ele).perform()
        driver.find_element(By.XPATH,"//div[@class='action-wrap']").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"(//span[text()=' ETH '])[2]").click();
        time.sleep(2)
        driver.find_element(By.XPATH,("//input[contains(@class,'w-70 border-none')]")).clear();
        time.sleep(2)
    except:
        pass
    

def CancelOrder(driver):
    # cancel order
    driver.find_element(By.XPATH,"//span[text()=' Cancel All ']").click();
    time.sleep(1)
    driver.find_element(By.XPATH,("//span[text()=' Yes, cancel all ']")).click();
    time.sleep(1)

def OTC(driver):
    driver.get(f"{env}/en/otc")
    time.sleep(4)

    # fiat buy
    driver.find_element(By.XPATH,"//button[contains(@class,'drop-down-bar-wrap drop-down-bar')]").click();
    search = ActionChains(driver)
    search.send_keys(New_Coin).perform()
    driver.find_element(By.XPATH,"//div[contains(@class,'text-layout flex-box')]").click();
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@class='otc-input otc-form__input']//input").send_keys(1);
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[contains(@class,'otc-button otc-panel-form__button')]").click();
    time.sleep(1)
    driver.find_element(By.XPATH,"(//span[contains(@class,'otc-button footer-btn')])[2]").click();
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()=' ok ']").click();
    time.sleep(1)

    # crypto buy
    driver.find_element(By.XPATH,"(//button[contains(@class,'drop-down-bar-wrap drop-down-bar')])[2]").click();
    search = ActionChains(driver)
    search.send_keys(crypto).perform()
    time.sleep(1)
    driver.find_element(By.XPATH,"(//h4[text()='"+crypto+"'])[2]",).click();
    time.sleep(1)
    driver.find_element(By.XPATH,"(//span[contains(@class,'otc-button otc-panel-form__button')])").click();
    time.sleep(1)
    driver.find_element(By.XPATH,"(//span[contains(@class,'otc-button footer-btn')])[2]").click();
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()=' ok ']").click();
    time.sleep(1)

    # stablecoin buy
    driver.find_element(By.XPATH,"(//button[contains(@class,'drop-down-bar-wrap drop-down-bar')])[2]").click();
    search = ActionChains(driver)
    search.send_keys(stablecoin).perform()
    time.sleep(1)
    driver.find_element(By.XPATH,"(//h4[text()='"+stablecoin+"'])[2]").click();
    time.sleep(1)
    driver.find_element(By.XPATH,"(//span[contains(@class,'otc-button otc-panel-form__button')])").click();
    time.sleep(1)
    driver.find_element(By.XPATH,"(//span[contains(@class,'otc-button footer-btn')])[2]").click();
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()=' ok ']").click();
    time.sleep(1)

    # change to sell
    driver.find_element(By.XPATH,"//div[@class='tab item-sell']").click() 
    time.sleep(2)

    # fiat sell
    driver.find_element(By.XPATH,"(//button[contains(@class,'drop-down-bar-wrap drop-down-bar')])[2]").click()
    search = ActionChains(driver)
    search.send_keys(fiat).perform()
    time.sleep(1)
    driver.find_element(By.XPATH,"//h4[text()='"+fiat+"']").click();
    driver.find_element(By.XPATH,"(//input[@placeholder='-'])[2]").click();
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@class='otc-input-block-input__input']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@class='otc-input-block-input__input']").send_keys("1")
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[contains(@class,'otc-button otc-panel-form__button')]").click();
    time.sleep(1)
    driver.find_element(By.XPATH,"(//span[contains(@class,'otc-button footer-btn')])[2]").click();
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()=' ok ']").click();
    time.sleep(1)

    # crypto sell
    driver.find_element(By.XPATH,"(//button[contains(@class,'drop-down-bar-wrap drop-down-bar')])[2]").click();
    search = ActionChains(driver)
    search.send_keys(crypto).perform()
    time.sleep(1)
    driver.find_element(By.XPATH,"(//h4[text()='"+crypto+"'])[2]").click();
    driver.find_element(By.XPATH,"(//input[@placeholder='-'])[2]").click();
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@class='otc-input-block-input__input']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@class='otc-input-block-input__input']").send_keys("1")
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[contains(@class,'otc-button otc-panel-form__button')]").click();
    time.sleep(1)
    driver.find_element(By.XPATH,"(//span[contains(@class,'otc-button footer-btn')])[2]").click();
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()=' ok ']").click();
    time.sleep(1)
    # stablecoin sell
    driver.find_element(By.XPATH,"(//button[contains(@class,'drop-down-bar-wrap drop-down-bar')])[2]").click();
    search = ActionChains(driver)
    search.send_keys(stablecoin).perform()
    time.sleep(1)
    driver.find_element(By.XPATH,"(//h4[text()='"+stablecoin+"'])[2]").click();
    driver.find_element(By.XPATH,"(//input[@placeholder='-'])[2]").click();
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@class='otc-input-block-input__input']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@class='otc-input-block-input__input']").send_keys("1")
    driver.find_element(By.XPATH,"//span[contains(@class,'otc-button otc-panel-form__button')]").click();
    time.sleep(1)
    driver.find_element(By.XPATH,"(//span[contains(@class,'otc-button footer-btn')])[2]").click();
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()=' ok ']").click();
    time.sleep(1)

def Convert(driver):
    driver.get(f"{env}/en/convert")
    time.sleep(3)
    driver.find_element(By.XPATH,"(//button[@type='button'])[2]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"(//input[@class='search__input'])").send_keys(New_Coin)
    time.sleep(2)
    driver.find_element(By.XPATH,("//h4[text()='"+New_Coin+"']")).click();
    driver.find_element(By.XPATH,"//input[@class='input-inline-input']").send_keys(1)
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[@class='convert__button convert__button-enabled']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[contains(@class,'body__button btse-button')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//div[@class='convert__input-container']/following-sibling::button[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[@class='convert__button convert__button-enabled']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"(//span[@class='button-content'])[2]").click();
    time.sleep(2)

    #crypto
    driver.find_element(By.CLASS_NAME,"convert__transfer-button").click()
    driver.find_element(By.XPATH,"(//button[contains(@class,'drop-down-bar-wrap drop-down-bar')])[2]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"(//input[@class='search__input'])[2]").send_keys(crypto)
    time.sleep(2)
    driver.find_element(By.XPATH,"(//h4[text()='"+crypto+"'])[2]").click()
    driver.find_element(By.XPATH,"//button[@class='convert__button convert__button-enabled']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[contains(@class,'body__button btse-button')]").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME,"convert__transfer-button").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@class='input-inline-input']").clear()
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@class='input-inline-input']").send_keys('0.00001')
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[@class='convert__button convert__button-enabled']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[contains(@class,'body__button btse-button')]").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME,"convert__transfer-button").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"(//button[contains(@class,'drop-down-bar-wrap drop-down-bar')])[2]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"(//input[@class='search__input'])[2]").send_keys(stablecoin)
    time.sleep(2)
    driver.find_element(By.XPATH,"(//h4[text()='"+stablecoin+"'])[2]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@class='input-inline-input']").clear()
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@class='input-inline-input']").send_keys('1')
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[@class='convert__button convert__button-enabled']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[contains(@class,'body__button btse-button')]").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME,"convert__transfer-button").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[@class='convert__button convert__button-enabled']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[contains(@class,'body__button btse-button')]").click()
    time.sleep(2)

def ChangeWallet(driver):
    #change to wallet
    driver.get(f"{env}/en/wallets/spot")
    time.sleep(3)

def Sendto(driver):
    driver.find_element(By.XPATH,("(//div[@class='item']/following-sibling::div)[3]")).click()
    time.sleep(1)
    driver.find_element(By.XPATH,("(//button[contains(@class,'drop-down-bar-wrap drop-down-bar')])[2]")).click();
    time.sleep(1)
    driver.find_element(By.XPATH,("(//input[@class='search__input'])[2]")).send_keys(New_Coin);
    time.sleep(1)
    driver.find_element(By.XPATH,("//h4[text()='"+New_Coin+"']")).click();
    time.sleep(1)
    driver.find_element(By.CLASS_NAME,("input-inline-input")).send_keys("1");
    time.sleep(1)
    driver.find_element(By.XPATH,("//input[@placeholder='Enter username']")).send_keys("xitayo9939");
    driver.find_element(By.XPATH,("//input[@placeholder='Enter email']")).send_keys("xitayo9939@upsdom.com");
    driver.find_element(By.XPATH,("//button[contains(@class,'next-btn btse-button')]")).click();
    token = totp.now()
    driver.find_element(By.CLASS_NAME,("input-inline-input")).send_keys(token);
    time.sleep(2)
    driver.find_element(By.XPATH,("//button[contains(@class,'flow-dialog__button btse-button')]")).click();

def History(driver):
    driver.get(f"{env}/en/history/spot/currency?type=wallet&currency="+New_Coin+"")
    time.sleep(5)
    driver.get(f"{env}/en/history/spot/currency?type=trade&currency="+New_Coin+"")
    time.sleep(5)
    pass

def main():
    option = webdriver.ChromeOptions()
    path = Service("./chromedriver")
    driver = webdriver.Chrome(service=path,options=option)
    driver.maximize_window()
    Login(driver)
    ChangeCoin(driver)
    USD(driver)
    BTC(driver)
    ETH(driver)
    CancelOrder(driver)
    Convert(driver)
    OTC(driver)
    ChangeWallet(driver)
    Sendto(driver)
    History(driver)
    time.sleep(3)
    driver.quit()

main()