from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time
import telebot
import subprocess

url1 = ["https://telefonicachile.grafana.net/d/zRgowkESk2/opsti-procesos-reposiciones?orgId=1&refresh=1m",
        "https://telefonicachile.grafana.net/d/KmjrqDAVz/opsti-procesos-ordenesoms?refresh=1m&orgId=1",
        "https://telefonicachile.grafana.net/d/DVOoqv0Vz/opsti-app-esb-errorscount?refresh=1m&orgId=1&from=now-3h&to=now",
        "https://telefonicachile.grafana.net/d/G0ZK3v0Vk/opsti-app-turbocharging-rb-tps?refresh=1m&orgId=1",
        "https://telefonicachile.grafana.net/d/647kYyjVz/opsti-amdocs-lockservers-register?orgId=1&refresh=5m",
        "https://telefonicachile.grafana.net/d/QqwAev0Vz/opsti-procesos-trb?refresh=1m&orgId=1"]

def register_grafana_commands(bot):
    @bot.message_handler(commands=['grafana'])
    def ejecucion(message):
        try:
            i=0
            for c in url1:
                options = webdriver.ChromeOptions()
                options.add_argument('--no-sandbox')
                options.add_argument('--window-size=1024,1080}')
                options.add_argument('--headless')
                options.add_argument("--hide-scrollbars")
                options.add_argument('--disable-gpu')
                options.add_argument('--ignore-certificate-errors')
                options.add_experimental_option("excludeSwitches", ["enable-automation"])
                options.add_argument("user-data-dir=C:\\Users\\Jose\\Application Data")
                driver = webdriver.Chrome(options=options)
                
                driver.maximize_window()
                driver.get(c)
                time.sleep(5)
                xpath_expression = '//*[@id="pageContent"]/div[3]/div/div/div/div[1]/div/h1'
                                            
                try:
                    driver.find_element("xpath" , xpath_expression)
                    driver.find_element("xpath" , '//*[@id="pageContent"]/div[3]/div/div/div/div[2]/div/div/a').click()
                    time.sleep(2)
                except NoSuchElementException:
                    print("El elemento no existe, entonces no hay que dar click a iniciar.")
                
                time.sleep(2)    
                screenshot = driver.save_screenshot(f'C:/Users/Jose/Downloads/screenshots/captura_{i}.png')
                i+=1
                time.sleep(2)
                driver.close()
            driver.quit()
            
            bot.reply_to(message, "Captura de pantalla Grafana guardadas...")
            
            imagenes = [0,1,2,3,4,5]
            for i in imagenes:
                photo = open(f'C:/Users/Jose/Downloads/screenshots/captura_{i}.png', 'rb')
                bot.send_photo(message.chat.id, photo)
        except Exception as e:
            bot.reply_to(message, f'Error: {str(e)}')