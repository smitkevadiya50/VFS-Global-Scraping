from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os

url = "https://visa.vfsglobal.com/ind/en/deu/login"
user_email="Email"
user_password="Password"
iplist = []
portlist= []
ipT = open("Jupyter/iplist.txt", "r")
portT = open("Jupyter/portlist.txt", "r")
pro = ''
bookButton = 1
for v in ipT:
    iplist.append(v.removesuffix('\n'))

for v in portT:
    portlist.append(v.removesuffix('\n'))

while True:
    try:
        firefox_options = Options()
        # open in headless mode to run in background
        firefox_options.headless = True
        # firefox_options.add_argument("start-maximized")
        # following options reduce the RAM usage
        firefox_options.add_argument("disable-infobars")
        firefox_options.add_argument("--disable-extensions")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-application-cache")
        firefox_options.add_argument("--disable-gpu")
        firefox_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        firefox_options.add_experimental_option('useAutomationExtension', False)
        firefox_options.add_argument("--disable-blink-features=AutomationControlled")
        firefox_options.add_argument("--disable-dev-shm-usage")
        firefox_options.add_argument("--incognito")
        driver = webdriver.Chrome(r"Your Path\chromedriver.exe",options=firefox_options)
        driver.delete_all_cookies()
            # make sure that the browser is full screen, else some buttons will not be visible to selenium
        driver.maximize_window()
        # open the webpage
        driver.get(url)
        time.sleep(20)
        print("Load Website")
        #reject Coocki
        driver.find_element(By.XPATH,'//*[@id="onetrust-reject-all-handler"]').click()
        print("Reject Cookies")
        #Login
        email = driver.find_element(By.XPATH, '//*[@id="mat-input-0"]')
        email.send_keys(user_email)
        passs = driver.find_element(By.XPATH, '//*[@id="mat-input-1"]')
        passs.send_keys(user_password)
        driver.find_element(By.XPATH,'/html/body/app-root/div/app-login/section/div/div/mat-card/form/button').click()
        print("Login Account")
        time.sleep(50)
        #/html/body/app-root/ngx-ui-loader/div[1]/div[1]/div
        #Book Button
        driver.find_element(By.XPATH, '//*[@id="mat-tab-content-0-0"]/div/div/div/div[3]/div[2]/span').click()
        print("Book Now: total Button Click: - "+ str(bookButton) +  "items")
        bookButton = bookButton+1
        time.sleep(20)
        #check Slot
        web_date =driver.find_element(By.XPATH, '/html/body/app-root/div/app-book-appointment/section/mat-card[1]/div[2]/div/div/full-calendar/div[1]/div[1]/h2')
        if web_date.text == 'October 2022':
            print("Go back")
            driver.find_element(By.XPATH, '/html/body/app-root/div/app-book-appointment/section/mat-card[1]/div[2]/div/div/full-calendar/div[1]/div[3]/div/button[1]').click()
            time.sleep(15)  
        availibleDate = driver.find_elements(By.CLASS_NAME,"date-availiable")
        if(len(availibleDate)!=0):
            print(time.strftime("%m-%d-%Y %I:%M:%p"))
            os.system('start Jupyter/stream.mp3')
            for item in availibleDate:
                print("Date is available  at:-" + item.text )
        else:
            print("Date is not available at:-" + time.strftime("%m-%d-%Y %I:%M:%p"))
            time.sleep(10)
        #logout
        driver.find_element(By.XPATH, '//*[@id="navbarDropdown"]').click()
        time.sleep(1)
        print("LogOut....")
        driver.find_element(By.XPATH, '/html/body/app-root/header/div[1]/div/div/ul/li/div/a[2]').click()
        driver.delete_all_cookies()
        driver.close()
        driver.quit()
        print("sleeping for 6:60 min")
        time.sleep(660)
    except Exception as e:
        print("some error " + time.strftime("%m-%d-%Y %I:%M:%p"), e)
        print("-----------------------------------------------------")
        print("Error Time:-" + time.strftime("%m-%d-%Y %I:%M:%p"))
        break


