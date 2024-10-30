from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyautogui
import telebot
import time

def register_apm_commands(bot):
    @bot.message_handler(commands=['apm'])
    def ejecucion_apm(message):
        try:
            # URL que deseas capturar
            url = "http://apmtc.tchile.local:8080/#console;db=Oveview+Believe;dn=SuperDomain;mm=FullStack;tr=0"

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
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.press('tab')
            time.sleep(1)
            with open('D:\\repositorio\\chatbot-telegram-python\\password_apm.cfg', 'r') as secreto:
                usuario = secreto.readline().strip()
                passwd = secreto.readline().strip()
            pyautogui.write(usuario)
            time.sleep(1)
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.write(passwd)
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(25)
            screenshot = driver.save_screenshot('C:/Users/Jose/Downloads/screenshots/captura_APM.png')
            driver.quit()
            bot.reply_to(message, "Captura de pantalla APM guardada...")
            photo = open('C:/Users/Jose/Downloads/screenshots/captura_APM.png', 'rb')
            bot.send_photo(message.chat.id, photo)
        except Exception as e:
            bot.reply_to(message, f'Error: {str(e)}')