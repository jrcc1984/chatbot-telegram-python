#from email import message
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import telebot
import time

def register_uim_commands(bot):
    @bot.message_handler(commands=['uim'])
    def ejecucion_uim(message):
        try:
            # URL que deseas capturar
            url = "http://monitoruim.tchile.local/dashboard/jsp/standalone.jsp?path=COMMAND_CENTER/%20Dashboard_Summary"
            
            options = webdriver.ChromeOptions()
            options.add_argument('--no-sandbox')
            options.add_argument('--window-size=1024,720}')
            #options.add_argument('--headless')
            options.add_argument("--hide-scrollbars")
            options.add_argument('--disable-gpu')
            options.add_argument('--ignore-certificate-errors')
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_argument("user-data-dir=C:\\Users\\Jose\\Application Data")
            driver = webdriver.Chrome(options=options)

            driver.maximize_window()
            driver.get(url)
            time.sleep(2)
            username_field = driver.find_element("xpath", '//*[@id="usrname"]')
            username_field.send_keys("son_ams")
            time.sleep(1)
            password_field = driver.find_element("xpath", '//*[@id="pswd"]')
            password_field.send_keys("qwe12qwe")
            time.sleep(1)
            driver.find_element("xpath", '/html/body/div/form/div[1]/input').click()
            time.sleep(2)
            driver.find_element("xpath", '//*[@id="ui-id-6"]/tbody/tr[4]/td[1]/span/span[1]').click()
            time.sleep(2)
            driver.find_element("xpath", '//*[@id="ui-id-6"]/tbody/tr[6]/td[1]/span/span[3]').click()
            time.sleep(2)
            driver.find_element("xpath", '//*[@id="openBtn"]/span').click()
            time.sleep(2)
            screenshot = driver.save_screenshot('C:/Users/Jose/Downloads/screenshots/captura_UIM.png')
            time.sleep(1)
            driver.quit()
            bot.reply_to(message, "Captura de pantalla UIM guardada...")
            photo = open('C:/Users/Jose/Downloads/screenshots/captura_UIM.png', 'rb')
            bot.send_photo(message.chat.id, photo)
        except Exception as e:
            bot.reply_to(message, f'Error: {str(e)}')